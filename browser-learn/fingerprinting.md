# **Browser Fingerprinting**

* It identifies users uniquely and their associate sessions regardless of anonymizing tactics like incognito browsing, VPNs, and cookie blockers.
* Unlike deleting cookies, a user cannot change their browser fingerprint.
* Fingerprinting can identify trends of malicious behavior and block you next time.

## Data taken through fingerprinting:

- Fingerprinting doesnt need your ip address or cookie to identify you:
- **It uses these identifiers:**

* Computer make and model
* Operating system version
* Browser version
* Browser extensions
* Timezone
* Language settings
* Adblocker used
* Screen size and resolution
* Tech specs (CPU, GPU, hard disk, etc.)

- By processing these details, it creates a unique identifier, or "digital fingerprint," for each user. This identifier remains consistent across different browsing sessions, making it a reliable tool for visitor identification beyond the realm of traditional cookies.
- Through fingerpriting you are given a unique profile and thus labelled a *unique visitor*
- [High-level browser fingerprinting](https://fingerprint.com/blog/browser-fingerprinting-techniques/) can be used to gather specific information, or signals, about a visitor that are then used to identify anonymous visitors upon returning to the website or app. Collecting multiple signals allows an anonymous user to be correctly identified, even if things like IP addresses or browsers change.


## Browser Fingerprinting Techniques:

### Canvas Fingerprinting:

- This browser fingerprinting technique uses the HTML5 canvas element to identify variances in a user’s GPU, graphics drivers, or graphics card.
- First, the script draws an image, often overlaid with text. Then, the script captures how the user’s web browser has rendered the image and text. Naturally, every device with different hardware and drivers will render the image slightly differently, distorting its color and shape. A hash is then computed using the rendered image’s data, which serves as the ‘canvas fingerprint.’

**N/B** 

**READ MORE**

https://fingerprint.com/blog/browser-fingerprinting-techniques/

https://amiunique.org/
