#!/usr/bin/env python3
"""BM25-ranked keyword search over pages/*.md.

Usage:
    python scripts/search.py "<query>" [--top N]

Pure stdlib (tokenize -> term frequency -> inverse document frequency
-> standard BM25 scoring, k1=1.5, b=0.75). This is not semantic search
-- it only matches words that actually appear in a page's title or
body -- but ranking by BM25 beats grep for a corpus this size: it
handles multi-word queries, weights rare terms over common ones, and
returns a ranked top-N instead of every substring hit.

Approach adapted from devops-shared-memory's framework/scripts/search.py
(pure-stdlib BM25 over a small local corpus); reimplemented here
against this repo's own page/frontmatter shape rather than imported,
since the two corpora (episodic memory entries vs. wiki pages) differ
enough that sharing the module wasn't worth a cross-repo dependency
for ~150 lines.
"""

import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _pages  # noqa: E402

TOKEN_RE = re.compile(r"[a-z0-9]+")
K1 = 1.5
B = 0.75


def tokenize(text):
    return TOKEN_RE.findall(text.lower())


def build_corpus():
    docs = []
    for name, fields, body in _pages.iter_pages():
        title = fields.get("title", "")
        tokens = tokenize(" ".join([title, body]))
        docs.append({"name": name, "title": title, "tokens": tokens, "length": len(tokens)})
    return docs


def bm25_rank(docs, query, top_n):
    query_terms = tokenize(query)
    n_docs = len(docs)
    if n_docs == 0 or not query_terms:
        return []

    avgdl = sum(d["length"] for d in docs) / n_docs

    doc_freq = {}
    term_freqs = []
    for d in docs:
        tf = {}
        for tok in d["tokens"]:
            tf[tok] = tf.get(tok, 0) + 1
        term_freqs.append(tf)
        for term in set(query_terms):
            if tf.get(term, 0) > 0:
                doc_freq[term] = doc_freq.get(term, 0) + 1

    idf = {}
    for term in set(query_terms):
        n_qi = doc_freq.get(term, 0)
        idf[term] = math.log((n_docs - n_qi + 0.5) / (n_qi + 0.5) + 1)

    scored = []
    for d, tf in zip(docs, term_freqs):
        score = 0.0
        dl = d["length"] or 1
        for term in query_terms:
            f = tf.get(term, 0)
            if f == 0:
                continue
            numerator = f * (K1 + 1)
            denominator = f + K1 * (1 - B + B * dl / avgdl)
            score += idf[term] * (numerator / denominator)
        if score > 0:
            scored.append((score, d))

    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:top_n]


def main():
    args = [a for a in sys.argv[1:] if a != "--top"]
    top_n = 10
    if "--top" in sys.argv:
        idx = sys.argv.index("--top")
        top_n = int(sys.argv[idx + 1])
        args = [a for a in sys.argv[1:] if a not in (sys.argv[idx], sys.argv[idx + 1])]

    if len(args) != 1:
        print(__doc__)
        return 1
    query = args[0]

    docs = build_corpus()
    results = bm25_rank(docs, query, top_n)

    if not results:
        print("No results.")
        return 0

    for score, d in results:
        print(f"{score:6.3f}  {d['title']}  [pages/{d['name']}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
