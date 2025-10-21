# graphDee — A Freelance Graphic Design Store

## Project Overview
**graphDee** is a simple full-stack web app where customers can purchase custom graphic design work. Visitors can browse a showcase gallery; registered users can place an order, see a live price preview (JS), pay in Stripe test mode, and track orders. Staff can upload completed work for the customer to download.

This project satisfies typical Django full-stack requirements: multiple apps, relational models, authentication, forms with validation, Stripe payments, JavaScript UX, version control, documentation, and (optional) deployment.

---

## Purpose

### Business Goals
- Let customers place and pay for design orders easily.
- Showcase past work and testimonials to build trust.
- Provide a simple internal flow for fulfilling and delivering designs.
- Deploy when the MVP is stable to enable demos and feedback.

### Target Users
- **Prospective customers** evaluating design quality and pricing.
- **Paying users** who need custom graphics (logo, poster, icon).
- **Site owner (designer)** delivering files and managing orders.

### User Needs
- Clear gallery of previous work and results.
- Simple order form with a predictable pricing model.
- Secure, familiar checkout (Stripe test mode).
- A dashboard to see order status and download results.
- For the designer: easy upload/delivery and basic admin tools.

---

## User Stories Overview
1. **Authentication**: As a user, I can sign up, log in, and log out to access ordering and my dashboard.
2. **Gallery**: As a visitor, I can browse previous work and testimonials to decide to buy.
3. **Order & Pay**: As a logged-in user, I can place an order, preview price (JS), and pay (server-verified price via Stripe).
4. **Delivery**: As staff, I can upload finished designs and mark orders as completed; as a customer, I can download.
5. *(Stretch)* **Feedback**: As a customer, I can accept results or request changes and submit a testimonial that appears in the gallery.

---

## Website Structure

### Menu
- **Home** (`/`) — Gallery and landing CTA.
- **Order** (`/orders/`) — Order form + Stripe checkout.
- **My Orders** (`/orders/my/`) — Past orders, statuses, downloads.
- **Login/Signup/Logout** — Allauth routes under `/accounts/`.
- **Admin** (`/admin/`) — Django admin for staff.

### Wireframes

**Homepage**


## Features
- **Authentication** via `django-allauth` (email or username).
- **Gallery** of previous designs with optional testimonial text.
- **Order form** with server-validated pricing and client-side preview.
- **Stripe Checkout** (test mode) with server-calculated price.
- **My Orders** page for users (see history, status, download result).
- **Admin delivery**: staff uploads completed files and marks status.
- **Dark theme** with Google Fonts (Akaya Kanadaka / Shadows Into Light Two / Spectral) and **Bootstrap** for responsive layout.
- **Static/Media handling** with WhiteNoise (static) and Django media.

---

## Technologies Used

#### Languages Used
- HTML  
- CSS  
- JavaScript


#### Frameworks, Libraries & Programs Used
- VS Code for local development https://code.visualstudio.com/
- Github for saving and storing files, and version control https://github.com/
- Canva for images and wireframes https://www.canva.com/
- Preview Editor app in MacBook for editing photos https://preview.app/login
- IMAGECOLORPICKER.com to choose color palette https://imagecolorpicker.com/
- Squoosh for converting image file types from png/jpg to. webp https://squoosh.app/
- Google Fonts for typography https://fonts.google.com/
- Font Awesome for icons https://fontawesome.com/
- Favicon.io for generation of favicons https://favicon.io/
- Bootstap Version 5.3 for styling/layout https://getbootstrap.com/
Autoprefixer for CSS versatility https://autoprefixer.github.io/
The W3C CSS Validation Service to review codes https://www.w3.org/
Nu Html Checker to review codes https://validator.nu/
WebAIM: Contrast Checker to verify contrast for color palette https://webaim.org/resources/contrastchecker/

- **Python** 
- **Django** 
- **django-allauth** 
- **Stripe** (Checkout Sessions, SDK)
- **SQLite** (dev), **PostgreSQL** in production via `psycopg2-binary`
- **Gunicorn**, **WhiteNoise**
- **Pillow**
- **Bootstrap 5**
- Minimal custom **JavaScript** (price preview)
- **Git & GitHub**


### Deployment & Local Development
Github Repo: https://github.com/limcaroline/graphdee

#### How to create repo in Github for deployments
I first followed these steps from Code Institute module to create a repo in github:
1. Log into www.github.com. Click the plus icon and select New repository.
2. Name the repository accordingly - Note: I used travel-world.
3. Select Create repository.
4. Copy the commands from … or create a new repository on the command line.
5. In VS Code, use "Open folder" from the file menu to open your vscode-projects folder and create a new project directory.
6. Open a new terminal, and paste in the commands copied from GitHub.
7. You should now see the README.md file appear in the Explorer.

#### How to Deploy 
These are the steps to deploy in github that I followed, also referenced from Code Institute's module:

From VSCode, commit and push all your changes to Github.
Go to GitHub repo https://github.com/limcaroline/graphdee, select Settings, then Pages.
Select the main branch and then Save.
In the Code tab, select Deployments.
On the Deployments page, refresh until the link is provided.
Click the link to check that it is working

#### How to Fork
In Github, go to this Repository: https://github.com/limcaroline/graphdee
Click the Fork button at the top right of this page to create your own copy of the repo.

#### How to Clone
In Github, go to this Repository: https://github.com/limcaroline/graphdee
Click the green Code button.
Copy the URL under "HTTPS".
Open your terminal.
Run this command: git clone https://github.com/limcaroline/graphdee



---


### Testing
See TESTING.md 



### Stretch Goals



### Future Enhancements
More detailed pricing options (colors, turnaround, vector source).
Change Requests: a one-click “Request changes” status (single revision round).
Accept + Testimonial: save testimonial and auto-add final image to Gallery.

### Credits

Django — https://www.djangoproject.com/

django-allauth — https://django-allauth.readthedocs.io/

Stripe — https://stripe.com/

Bootstrap — https://getbootstrap.com/

WhiteNoise — https://whitenoise.evans.io/

Pillow — https://python-pillow.org/


Media

See also Frameworks, Libraries & Programs Used for more references
Canva for images
Bootstap Version 5.3 for styling/layout
Google Fonts for typography
Font Awesome for icons
Code

Bootstrap for cards and similar, also see comments in VSCode https://getbootstrap.com/
Code Institute's modules, including BoardWalk Games and Love Running https://learn.codeinstitute.net/dashboard
ChatGPT for helping with ideas, debugging, and structuring https://chatgpt.com/
Autoprefixer for code prefix on transition

Acknowledgments

Big thanks to Code Institute’s team as well as materials and Level 5 Diploma in Web Application Development modules and walkthrough projects, which I have used as references!
Special thanks to ChatGPT by OpenAI for assistance in troubleshooting and debugging, as well as support in ideas and structure.
Thank you to all the mentioned in this readme and in VScode that was helpful in making this project!