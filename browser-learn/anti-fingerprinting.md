# **1. LetterBoxing:**

- Letterboxing is a browser feature that adds gray bars around the web view to hide your browser dimensions.
- To correctly render a webpage, your browser needs to know your window size. Letterboxing forces your browser window dimensions to be multiples of 100 or 50 pixels and fills the extra space with gray bars on the sides of the page. This makes your browser window size more common, such as 1200px x 900px, instead of exposing a more specific window size like 1231px by 895px, placing you into a large group of people with similar-sized browsers instead of singling you out.

### How can you turn letterboxing on?

To turn on letterboxing in Firefox, go to about:config, create a new setting privacy.resistFingerprinting.letterboxing, and set it to true.

In Tor Browser, letterboxing is enabled by default.
