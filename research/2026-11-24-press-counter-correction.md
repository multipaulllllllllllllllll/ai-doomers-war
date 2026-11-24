# November 24: chronology press-counter correction

The owner identified stale Jensen press-review counts on the chronology. Inspection confirmed the chronology teaser retained 48 pieces, 12 outlets, 38 reporting/analysis, one editorial and nine signed opinion pieces. The standalone collection contains 65 article records from 18 outlets: 53 reporting/analysis, three editorial-board pieces and nine signed opinion pieces.

Scope: replace only the chronology's press-feature aside, deriving the counters from the current standalone collection. Preserve all chronology cards, monthly counts and the standalone collection. Add a synchronization/check script so this mismatch can be detected before later publication. Do not run the historical press renderer: its source and fixed 48-piece assertion would overwrite the updated collection.

Verification: compare actual article counts and distinct data-outlet values against both displays, assert that every byte outside the teaser is unchanged, and fetch both live pages after publication.
