# Provider and Filing Definition Check

Use this pre-staged route during Lab 01 so validation is a bounded read-and-cite task rather than
an open web search.

## Price-series configuration

Open the [yfinance `download` API reference](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html).
Locate the definitions for `period`, `interval`, `auto_adjust`, `actions`, `repair`, and `keepna`.
Compare them with `screening_starter.py`: three-year period, daily interval, `auto_adjust=False`,
`actions=False`, `repair` left at its default, and an explicit requirement for the returned
`Adj Close` field. Record the documentation page, access date, parameter checked, and conclusion.

This API reference establishes software-parameter behavior. It does **not** establish that a
returned price is correct, that all corporate actions were handled as intended, or that a
security is suitable for research.

## Company-fact route

For a real target fact, use the [SEC's official filing search](https://www.sec.gov/search-filings)
to locate the issuer's latest relevant 10-K, 10-Q, or 8-K. Record issuer, form, filing date,
reporting period, exact section/table, fact checked, and whether the screen label should be
accepted, qualified, or rejected. A search-result snippet or AI summary is not the source.

If network access fails, use the instructor's dated accessible print/PDF capture of these same
pages and label the check `offline source capture`. Never invent an access date or finding.
