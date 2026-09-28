# [twitcher_app](https://twitcher-app-0de26394518f.herokuapp.com)

Developer: Kieron Rostill-Fellows ([lion695](https://www.github.com/lion695))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/lion695/twitcher_app)](https://www.github.com/lion695/twitcher_app/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/lion695/twitcher_app)](https://www.github.com/lion695/twitcher_app/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/lion695/twitcher_app)](https://www.github.com/lion695/twitcher_app)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://twitcher-app-0de26394518f.herokuapp.com)

## Project Introduction and Rationale

**Twitcher App** is a responsive, feature-rich web application designed as a community-driven digital field log for birdwatchers and nature enthusiasts. Built using the Django framework, the platform allows users to seamlessly document live wildlife encounters, submit precise geographical sighting updates, add multimedia records, and share notes with a broader community of enthusiasts. By providing a clean timeline feed, robust search tools, and interactive media attachments, Twitcher App bridges the gap between field research and community discussion.

The platform targets a diverse demographic of outdoor enthusiasts, ranging from casual backyard birdwatchers to seasoned, competitive "twitchers" tracking rare migrations. For casual users, Twitcher App serves as an accessible digital diary to learn more about local species and keep a visual record of their outdoor activities. For dedicated birdwatchers, the platform is a high-utility tracking hub. It enables them to verify species data via community comments, monitor recent local activity grids, and instantly share time-sensitive observation logs while out in the field.

The inspiration behind choosing a bird-sighting platform stems from the rapid resurgence of interest in eco-tourism, local biodiversity, and citizen science. Traditional wildlife tracking methods often rely on cumbersome physical notebooks or fragmented social media groups where critical data gets buried instantly. I opted to develop Twitcher App to provide a centralized, open-access, and structured solution tailored to this niche. From a software engineering perspective, this theme offered the perfect opportunity to implement complex relational database management frameworks. It allows for the integration of secure multi-user CRUD profiles, cloud-based media storage pipelines via Cloudinary, robust frontend text formatting, and rigid pagination timeline controls. By focusing on a community nature theme, the project demonstrates how modern full-stack web applications can successfully transform a highly active, offline passion into a structured, engaging digital ecosystem.


🛑 README NOTES 🛑

Do not add a **Table of Contents** to your Markdown files. GitHub has these built-in automatically using the headers/hashtags.

Don't add screenshots for the README/TESTING into your `assets` or `static` folders. Create a new folder at the root-level called `documentation`. Consider creating sub-directories within `documentation` to handle things like `wireframes`, `features`, `validation`, `responsiveness`, etc.

Learn about Markdown Alerts (aka Callouts), a fairly new feature for GitHub Markdown files.
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts
Note: these are not visible within your README Previewer, and are only visible once you push the code to GitHub.

**Site Mockups**
*([amiresponsive](https://fireship.dev/amiresponsive?url=https://twitcher-app-0de26394518f.herokuapp.com), [techsini](https://techsini.com/multi-mockup), etc.)*
Having issues generating site mockups? This is likely due to security policies with your deployed site.
If you open up your DevTools, there may be an error referencing `X-Frame-Options`.

For Chrome users, head over to http://bit.ly/3iRPn4u and install the extension within your browser. Once installed, navigate back to the mockup site of your choice. You should find your site rendering in the various devices now.

Alternatively, open your project in Gitpod and run the server. Once the site is running, click the `Ports` tab from your Gitpod Terminal. Click the padlock on the appropriate port for your project (`Flask: 5000`, `Django: 8000`). This will make your local page public temporarily. Now, copy the URL of your live-preview page into the responsive tool above. You should find your site rendering in the various devices.

🛑 --- END ---- 🛑

![screenshot](documentation/screenshots/am_i_responsive.png)

source: [twitcher_app amiresponsive](https://ui.dev/amiresponsive?url=https://twitcher-app-0de26394518f.herokuapp.com)

> [!IMPORTANT]  
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

### The 5 Planes of UX [LO1.5]

#### 1. Strategy

**Purpose**
- Provide wildlife enthusiasts and twitchers with an intuitive digital log to create, manage, and track real-time bird sighting records and geographical observations.
- Offer a collaborative community space for peer birdwatchers to engage, review, and corroborating field notes through structured comments.

**Primary User Needs**
- **Field Observers/Twitchers**: Need a mobile-responsive platform to instantly log bird details (species name, text summaries, rich-text field notes, media imagery, and precise calendars) while out in the field [LO1.1, LO2.4].
- **Community Members**: Need the ability to safely view recent activity feeds, verify rare species records, and contribute field insight via community comments.
- **Site Visitors (Guests)**: Need to browse the public bird observation timeline feed cleanly without being forced to register immediately.

**Business & Platform Goals**
- Foster an active, data-accurate citizen science ecosystem dedicated to recording local avian biodiversity.
- Build a community matrix where rare sightings can be rapidly corroborated and verified by peers.
- Guarantee seamless, secure content management controls for record authors and platform administrators [LO2.2].

#### 2. Scope

**Functional Features**
- Full multi-user CRUD capability: Registered users can Create, Read, Update, and Delete their own bird sighting log entries [LO2.2].
- Cloud-hosted multimedia integration: Native streaming pipelines via Cloudinary to attach high-quality field imagery to sighting logs.
- Interactive Community Feedback: A relational nesting system allowing authenticated users to publish comments and corroborations underneath individual entries.
- Backend Validation Architecture: Comprehensive forms validation checking input compliance (such as enforcing mandatory date rules to prevent database exceptions) [LO2.4].
- Defensive UI Redirection: Custom-branded nature-themed `404` and `500` error templates to catch navigation faults and server exceptions gracefully [LO3.3].

#### 3. Structure

**Information Architecture**
- **Global Dynamic Navigation Header**: Responsive Bootstrap navbar providing rapid traversal to Home Feed, Log Sighting, Register, Login, and Sign Out, dynamically toggling links based on active user authentication states [LO1.1, LO3.2].
- **Visual Grid Hierarchy**: Sighting logs are organized in a clean multi-column card pattern, displaying core summary strings, author metadata badges, and high-impact imagery prominently for scannability [LO1.1].

**User Workflow Application Paths**
1. **Unauthenticated Guest**: Views the home chronological timeline → Explores detailed sighting profiles → Prompted to log in if attempting to access log forms or post comments.
2. **New Community Member**: Registers a secure profile via `django-allauth` → Logs in → Gains instant access to platform interactive states [LO3.1].
3. **Authenticated Observer**: Accesses the "Log Sighting" view → Fills out validation-enforced form criteria (including selecting calendar dates) → Submits log → Receives success alert and views entry live on the main dashboard feed [LO2.3, LO2.4].
4. **Record Author**: Navigates to their specific post → Enters secure update or delete paths → Accesses modification forms or triggers an absolute delete via a defensive UX JavaScript confirmation modal [LO2.2, LO3.3].

#### 4. Skeleton

**[Wireframes](#wireframes)** (Detailed cross-device UX blueprint schematics and layout wireframes are explicitly documented and linked inside the `documentation/wireframes/` folder repository [LO1.5]).
![screenshot](documentation/wireframes/Wireframes.png)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)**: A curated, high-accessibility palette leveraging rich foliage greens, slate text rows, and clean canvas card layers to reflect the outdoor nature theme of the app [LO1.1].
- **[Typography](#typography)**: Crisp, clean, modern typography weights scaled dynamically across varying device viewports using responsive typography principles to assist field workers accessing text screens outdoors [LO1.1].


### Colour Scheme [LO1.1]

The Twitcher App uses a carefully selected, nature-inspired palette to establish thematic continuity with birdwatching and the outdoors. These specific hex codes guarantee excellent element contrast across both dark and light sections, keeping readability high for field users checking text rows on mobile monitors outdoors.

I used [coolors.co](https://coolors.co) to generate the official application palette:

*   `#111827` (Slate Black / Charcoal) - Primary body text and semantic navigation headers.
*   `#198754` (Forest Green) - Primary theme branding color, main validation highlights, button actions, and bird logo assets.
*   `#DC3545` (Crimson Red) - Secondary defensive design alerts, deletion modals, and 500 error indicators [LO3.3].
*   `#FFC107` (Amber Gold) - Accent indicators, notification warning borders, and status tracking labels.
*   `#F8F9FA` (Off-White / Light Canvas) - Background layers and card body rows to provide clean contrast against dark typography.

![Application Palette Layout Map](documentation/screenshots/coolors.png)


### Typography and Icons [LO1.1]

To guarantee high readability standards across varying device screen sizes, clean typography and semantic vector icon libraries were carefully implemented throughout the user interface.

#### Typography
*   **Primary Headers and Titles**: The [Montserrat](https://google.com) font family was selected for all major system headlines, card titles, and branding rows. Its bold, geometric weights establish a strong visual hierarchy and immediate scannability for page titles.
*   **Body and Secondary Text**: The [Lato](https://google.com) font family was applied to all primary body copy, descriptive text rows, form field labels, and comment blocks. This clean, sans-serif typeface maintains excellent structural legibility on mobile viewports under outdoor glare.
*   **Fallback Stack**: Standard `sans-serif` system rules were set as a fallback layer across global style configurations to maintain interface cohesion if external web assets experience latency.

#### Interactive Icons
*   [Font Awesome 6 Libraries](https://fontawesome.com) were integrated across global templates to supply clear, accessible visual indicators. 
*   Icons are strategically paired with text strings (such as navigation controls, user profile indicators, form field headers, and social media anchor icons in the footer) to improve interface accessibility and intuitive traversal paths for all users.


- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

⚠️ INSTRUCTIONS ⚠️

If you've created wireframes or mock-ups, use this section to display screenshots of your wireframes. The example table below uses sample pages from the walkthrough project to give you some inspiration for your own project, so please adjust accordingly.

⚠️ --- END --- ⚠️

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Visual Interface Viewports and Layout Matrix [LO1.5]

The matrix table below links individual core production page layouts directly to their corresponding cross-viewport responsiveness captures stored inside your documentation workspace repository folders:

| Page / Component View | Mobile Viewport Capture | Desktop Viewport Capture |
| :--- | :--- | :--- |
| **Home Timeline Feed** | ![Home Page Mobile](documentation/wireframes/5_home_page_mobile.png) | ![Home Page Desktop](documentation/wireframes/1_home_page_desktop.png) |
| **Sighting Detail Page** | ![Sighting Detail Mobile](documentation/wireframes/6_sighting_detail_mobile.png) | ![Sighting Detail Desktop](documentation/wireframes/2_sighting_detail_desktop.png) |
| **About Biography Page** | ![About Page Mobile](documentation/wireframes/7_about_page_mobile.png) | ![About Page Desktop](documentation/wireframes/3_about_page_desktop.png) |
| **Authentication Forms** | ![Authentication Mobile](documentation/wireframes/8_sign_in_register_mobile.png) | ![Authentication Desktop](documentation/wireframes/4_sign_in_desktop.png) |
| **Global Layout Footer** | ![Footer Component Mobile](documentation/wireframes/9_footer_mobile.png) | *(Unified Multi-Device Asset)* |



## User Stories

## User Stories [LO1.3]

The development of the Twitcher App was strictly guided by user-centric Agile milestones. The matrix below documents the complete suite of User Stories mapped across the three primary system roles (Site Administrators, Registered Birders, and Public Guests) to outline expectations and verify implementation outcomes.

### User Stories Matrix Mapping

| Target (As a...) | Expectation (I would like to...) | Outcome (so that...) | Status |
| :--- | :--- | :--- | :--- |
| **Site Administrator** | Create, inspect, and moderate all community record logs from a central control hub | I can maintain platform data standards and clean up invalid wildlife entries. | **Done** |
| **Site Administrator** | Hard-delete or force-edit any public comment row | I can instantly remove inappropriate responses or spam from sighting threads. | **Done** |
| **Registered Birder** | Register a secure user account via standard authentication forms | I can become a verified member of the local citizen-science birding community [LO3.1]. | **Done** |
| **Registered Birder** | Log in and out of my active profile securely at any time | My authentication state is accurately reflected across all layout headers [LO3.2]. | **Done** |
| **Registered Birder** | Publish a new bird sighting log featuring titles, species criteria, locations, calendar dates, and images | I can share my field observations and stream wildlife photos safely to Cloudinary [LO1.2]. | **Done** |
| **Registered Birder** | Modify or update my existing bird observation entries | I can correct species identification mistakes or append rich-text field notes later [LO2.2]. | **Done** |
| **Registered Birder** | Delete my own bird logging records entirely | I can remove accidental entries, backed by a defensive design confirmation modal [LO3.3]. | **Done** |
| **Registered Birder** | Leave text comments and corroboration notes under peer sighting records | I can contribute to field note verifications and share knowledge with other twitchers. | **Done** |
| **Registered Birder** | Edit or retract my own comment text lines | I can correct typographical errors or clean up my personal conversational footprint. | **Done** |
| **Public Guest User** | Browse the main chronological timeline feed of bird sightings | I can explore recent local wildlife activity without being forced to sign up immediately. | **Done** |
| **Public Guest User** | Access detailed sighting profile screens to inspect media and rich-text field observations | I can check species sightings, view peer comments, and read field metadata details cleanly. | **Done** |
| **Public Guest User** | See explicit visual indicators prompting me to log in when trying to access forms | I understand that advanced interactive states are securely restricted to active members [LO3.3]. | **Done** |
| **All App Users** | View a branded, custom 404 error page if I navigate to an unmapped path | I am notified gracefully that I am lost and am provided an immediate link back to the home feed [LO3.3]. | **Done** |
| **All App Users** | Encounter a graceful 500 error card screen during unexpected server exceptions | The application uses defensive design to preserve layout cohesion instead of crashing out raw code [LO3.3]. | **Done** |


## Features [LO2.2]

The Twitcher App incorporates an array of robust, full-stack interactive features built to provide birdwatchers and field twitchers with an accessible, rapid-utility data-logging hub. Each capability focuses on delivering user-centric data integrity and explicit feedback [LO1.1].

### Existing Features Matrix

| Feature Module | Operational Value & Target Audience Purpose | Screenshot Evidence Reference [LO1.5] |
| :--- | :--- | :--- |
| **User Account Registration** | Account generation managed securely via `django-allauth`. Enables field observers to establish individual user profiles so they can contribute data [LO3.1]. | ![User Registration Page](documentation/screenshots/user_registration_page.png) |
| **Secure Sign In Authentication** | Verifies credentials, logs birders into active sessions, and dynamically shifts global navbar links to grant authorized CRUD permissions [LO3.2]. | ![User Login Page](documentation/screenshots/user_login_page.png) |
| **Explicit Session Sign Out** | Terminates authenticated user active sessions cleanly, clearing authorization session tokens and reverting access states to read-only guest filters [LO3.2]. | *(Handled via Secure Navbar Session Trigger Row)* |
| **Chronological Sighting Timeline** | The main home grid layout showcases summary bird cards including high-impact Cloudinary media, species titles, location metadata badges, and author logs [LO1.1]. | ![Home Timeline Feed Dashboard](documentation/screenshots/home_timeline.png) |
| **Comprehensive Observation Profile** | Provides expanded sighting details, enabling users to read full rich-text field notes, check specific observation dates, and scroll through community feedback [LO1.2]. | ![Sighting Detail Page Layout](documentation/screenshots/sighting_detail_page.png) |
| **Responsive Timeline Pagination** | Controls database query loads by slicing entries into paginated grid rows. Keeps mobile loading times fast for observers browsing field data on the move [LO1.1]. | *(Integrated into Home Feed Navigation Footer)* |
| **Log Bird Sighting (Frontend Create)** | Registered members access a dedicated frontend form to report live observations, attach titles, configure tags, and upload image payloads directly [LO1.2, LO2.2]. | *(Rendered on Form Submission Sheet Interface)* |
| **Backend Validation Date Picker** | Enforces structural integrity by embedding an HTML5 calendar date picker inside forms, preventing null values and eliminating database crashes [LO2.4]. | *(Configured inside SightingForm Widget Matrix)* |
| **Sighting Modification (Frontend Update)**| Authors access pre-populated frontend editing forms to refine species data, alter locations, or append field logs instantly without accessing admin dashboards [LO2.2]. | *(Rendered via Authorized Edit View Routing)* |
| **Defensive Record Wipe (Frontend Delete)**| Record owners can remove their data. The destructive action is guarded by a defensive JavaScript confirmation modal to avoid accidental data loss [LO3.3]. | *(Protected via UI Trigger Button Confirmation Modal)* |
| **Interactive Community Comments** | Tethers field comments and corroboration notes to individual parent posts using a relational **1:N** database mapping constraint, fostering citizen-science debate [LO2.1]. | ![Nested Peer Comments Component](documentation/screenshots/nested_peer_comments.png) |
| **About Biography Context Sheet** | Renders a clean markdown profile detailing the application's core citizen-science mission parameters and operational rationale [LO1.5]. | ![About Biography Page](documentation/screenshots/about_page.png) |
| **Real-Time Notification Alerts** | Leverages the Django Messages framework to trigger immediate, accessible alert popups at the top of the viewport on any database change (e.g., successful creation) [LO2.3]. | *(Fired dynamically across view state actions)* |
| **Custom Branded 404 Defensive Redirect**| Intercepts broken, dead, or unmapped URL path strings and reroutes users to a custom nature-themed card offering a fast link straight back to the home timeline [LO3.3]. | *(Rendered via Global Project handler404 views.py)* |
| **Custom Branded 500 Server Fallback** | Catches unexpected server runtime exceptions or database connectivity gaps gracefully, preserving template styling instead of exposing naked raw trace logs [LO3.3]. | *(Rendered via Global Project handler500 views.py)* |
| **Secure Production Cloud Deployment** | Fully deployed to Heroku with `DEBUG = False`. Leverages an isolated, untracked `env.py` schema layout to hide production keys from repository trees [LO6.1, LO6.3]. | *(Live Production Host Environment Dashboard)* |


### Future Features & Product Roadmap [LO1.3]

While the current Minimum Viable Product (MVP) provides a secure, fully verified, and highly stable full-stack data logging platform, the following features are planned for future development cycles to expand community utility and deepen intelligence integration:

*   **AI Regional Habitat Guide Generator (Deferred Sprint Milestone - `Won't Have`)**: Re-incorporate the automated regional habitat guide generator by integrating the OpenAI API or a specialized Hugging Face computer vision model. This will allow users to instantly generate localized species checklists, nesting tip matrices, and migration forecasts based on their logged bird coordinates [LO8.3].
*   **Interactive Sighting Map Grid (Geographical Filtering)**: Integrate the Leaflet.js or Google Maps API to plot logged bird sightings onto a dynamic, visual map interface. This will enable field observers to filter recent avian data based on geographic proximity or county borders.
*   **Avian Species Search and Tag Filters**: Introduce a high-performance frontend search indexing bar alongside categorical metadata tags (e.g., *Raptors*, *Waterfowl*, *Migratory*). This will allow twitchers to isolate specific records rapidly without scrolling the global chronological feed.
*   **Community Sighting Verification System ("Upvoting")**: Implement a peer-review voting counter mechanism underneath individual logs. This will allow verified community birders to securely "Upvote" or flag rare bird sightings, establishing an organic data-trust rating directly on the dashboard card.
*   **Nested Comment Threads & Direct Replies**: Upgrade the existing One-to-Many (`1:N`) commenting model to allow nested multi-tiered discussion replies [LO2.1]. This will enable observers to discuss specific field note details cleanly without cluttering the primary sighting profile.
*   **Time-Sensitive Email Subscriptions**: Connect live email pipelines via SendGrid to allow twitchers to subscribe to real-time alerts. Users would receive instant email notifications the moment an entry categorized as a "Rare Species Sighting" writes to the regional database tables.


## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. Used also to generate custom site logo and favicon file. |
| [![badge](https://img.shields.io/badge/Gemini-grey?logo=googlegemini&logoColor=#8E75B2)](https://gemini.google.com) | Help debug, troubleshoot, and explain things. |

⚠️ NOTE ⚠️

Want to add more?

- Tutorial: https://shields.io/badges/static-badge
- Icons/Logos: https://simpleicons.org
  - FYI: not all logos are available to use

🛑 --- END --- 🛑

## Database Design

### Data Model

# Data Architecture & Database Schema Documentation [LO2.1]

The diagram below reflects the final production relational database model structures for the Twitcher App ecosystem. It outlines the entity definitions, core attributes, precise data types, and structural validation constraints implemented to satisfy full-stack criteria metrics.

![Twitcher App Database ERD Schema](documentation\ERDs\DB_schema_and_relationships.png)

**Summary of Relational Constraints \[LO2.1\]**

*   **date\_spotted (Data Integrity Constraint)**: Inside the sightings\_sighting table, this attribute is explicitly configured as a Django DateField with a strict NOT NULL constraint. By pairing this backend rule with an interactive frontend HTML5 date picker calendar widget inside the SightingForm, the ecosystem guarantees that a user cannot submit an incomplete observation record, successfully eliminating database-level IntegrityError rule violations.
    
*   **Cascading Safety Filters (ON DELETE CASCADE)**: To enforce strict referential integrity across the entire relational tree, relational foreign key constraints are established using cascading deletions:
    
    *   The author\_id foreign key inside both the sightings\_sighting and sightings\_comment tables establishes a **One-to-Many (1:N)** link to the master auth\_user primary key. If a user deletes their profile card, all their associated wildlife entries and comment records are immediately cleared from disk.
        
    *   The sighting\_id foreign key inside the sightings\_comment table maps directly to the parent post row. If an operational bird log is removed by its author, all nested community verifications and comments are swept away automatically, preventing orphan data rows.
        
*   **Timeline Caching Logs (Temporal Constraints)**: The created\_on and updated\_on attributes are embedded directly into individual model matrices utilizing Django's auto\_now\_add and auto\_now automation hooks. This locks precise server timestamps down to the millisecond without requiring user entry, allowing the database query layer to seamlessly return chronologically sorted home timeline feeds.
    
*   **slug (Unique Field Index Constraint)**: The slug text string attribute within the sightings\_sighting model is configured with a strict unique=True modifier constraint. This indexes the column globally within the database grid, guaranteeing that clean, human-readable SEO search strings resolve to unique records without overlapping routes.


![screenshot](documentation/erd.png)

⚠️ INSTRUCTIONS ⚠️

Using your defined models, create an ERD with the relationships identified. A couple of recommendations for building your own free ERDs:
- [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)
- [Draw.io](https://draw.io)

Looking for an interactive version of your ERD? Consider using a [`Mermaid flowchart`](https://mermaid.live). To simplify the process, you can ask ChatGPT (or similar) the following prompt:

> ChatGPT Prompt:  
> "Generate a Markdown syntax Mermaid ERD using my Django models"  
> [paste-your-django-models-into-ChatGPT]

The "I Think Therefore I Blog" sample ERD in Markdown syntax using Mermaid can be seen below as an example.

**NOTE**: A Markdown Preview tool doesn't show the interactive ERD; you must first commit/push the code to your GitHub repository in order to see it live in action.

⚠️ --- END --- ⚠️

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    USER ||--o{ SIGHTING : "authors"
    USER ||--o{ COMMENT : "writes"
    SIGHTING ||--o{ COMMENT : "contains"

    USER {
        int id PK
        string username
        string password
        string email
        boolean is_staff
    }

    SIGHTING {
        int id PK
        string title
        string slug "UQ"
        string species_name
        string location_spotted
        date date_spotted
        text summary
        string image "CloudinaryURL"
        text notes "CKEditor"
        int author_id FK
        datetime created_on
        datetime updated_on
    }

    COMMENT {
        int id PK
        text body
        int sighting_id FK
        int author_id FK
        datetime created_on
        boolean approved
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqlVFFvmzAQ_iuWn0kUkgUSXrOsq7J0W9O8TEjIxRdiDXzINmsymv8-Q0oKGdUqzQ-I8_dxfPfd2SWNkQMNKKiPgiWKZaEKJbFru1nek-fnwQBLsrm9-fxwe3dDAhJSVpg9Kh3SPubi63q9vHuoiU9KGGjxLll6uDFKw4R8YXcyl01ULSENEZx8W7U3tVFCJqTQoCTLoAfKmdZPqHgPBBkTaXv_ETEFJonQkTZst2uwU1vZpZZ3qzPCpH3SdFok1oDt91ej2mgOsQAdvVFXijEzAmWkczQGOvVxZqB-9IEGDoboIsuYOvbkFRlLwKpapFhwIS1pe_-lK7DOINF2uOKtllwYVF1KZcd5WiLryqfVtTojMiCxAvvKI5S9cJHzK7jTh2aG_t2GWu8j8uM1U4tkb2zRf2v8D_3NELE8V_jr1ftaPHVoogSngVEFODQDZWfQhrSsSCE1e7DdptW5UMCLw4Az9XMQY1obLE_2-5zJH4hZk0JhkexpsGOpttHZs5fzfNlVIDmoBRbS0GDs1jloUNKDjcbecDKbf_D9iTeajFzfoUcaTOfD8dj13Pl0NvLmruefHPq7_uloOPOnTnUT4OYo40YF1DOwPl8o9b1y-gNW8VuG)

⚠️ RECOMMENDED ⚠️

Alternatively, or in addition to, a more comprehensive ERD can be auto-generated once you're at the end of your development stages, just before you submit. Follow the steps below to obtain a thorough ERD that you can include. Feel free to leave the steps below in the README for future use to yourself.

⚠️ --- END --- ⚠️

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

⚠️ TIP ⚠️

Consider adding screenshots of your Projects Board(s), Issues (open and closed), and Milestone tasks.

⚠️ --- END ---⚠️

[GitHub Projects](https://www.github.com/lion695/twitcher_app/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/lion695/twitcher_app/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/lion695/twitcher_app?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/lion695/twitcher_app/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/lion695/twitcher_app?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/lion695/twitcher_app/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://twitcher-app-0de26394518f.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.



Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/lion695/twitcher_app).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/lion695/twitcher_app.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/lion695/twitcher_app)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/lion695/twitcher_app).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

## Credits and Attributions

### Code and Technical Resources
* **Django Framework**: Core full-stack architecture built using the official [Django Documentation](https://djangoproject.com) for model setups, class-based views, and custom error routing handler structures.
* **Django-Allauth**: Authentication flows, secure frontend registration forms, and account sign-in loops configured by following the [Django-Allauth Documentation](https://allauth.org).
* **Bootstrap Framework**: Global visual user interface styling grids, forms decoration fields, and defensive alert card containers built using components from the [Bootstrap 5.3 Documentation](https://getbootstrap.com).
* **WhiteNoise Engine**: Production static file aggregation, caching configurations, and asset compression delivery managed via the [WhiteNoise Storage Documentation](https://readthedocs.io).
* **Font Awesome**: Accessible user interface vector icon anchors mapped globally from the [Font Awesome CDN Libraries](https://fontawesome.com).

### Media and Brand Branding Assets
* **Branding Graphics & Favicon**: Custom nature-themed green bird branding logotype elements and multi-device `favicon.ico` responsive asset groups designed and generated utilizing the [readdy.ai](https://readdy.ai) asset suite canvas platform.
* **Interface Blueprints**: High-definition interactive layout schematics and cross-device display blueprints mapped using [ChatGPT](https://chatgpt.com/).

### AI Tool Orchestration Acknowledgements
In alignment with modern software engineering practices, this application was developed in active collaboration with advanced AI assistants:
* **ChatGPT (OpenAI)**: Orchestrated during the initial planning phase to generate technical database blueprints, select structural relational diagrams, and prototype initial layout matrices.
* **Claude AI (Anthropic)**: Leveraged throughout the main execution cycle as an active full-stack coding partner. Claude assisted in debugging live deployment asset paths, generating syntactically sound automated Django unit tests (`sightings/tests.py`), correcting `IntegrityError` form constraints, and structuring descriptive project markdown logs.



### Content

Eventually you'll want to learn how to use Git branches. Here's a helpful tutorial called [Learn Git Branching](https://learngitbranching.js.org) to bookmark for later.



| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
    - [Button Clicks](https://www.zapsplat.com/sound-effect-category/button-clicks)
    - [Lasers & Weapons](https://www.zapsplat.com/sound-effect-category/lasers-and-weapons/page/5)
    - [Puzzle Music](https://soundimage.org/puzzle-music)
    - [Camtasia Audio](https://library.techsmith.com/camtasia/assets/Audio)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.



| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [I Think Therefore I Blog](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [ChatGPT](https://chatgpt.com/) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project. Master classes that I attended with him really helped put things into perspective and he was always on hand if needed.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues. In particular my cohort facilitator Marko Tot who's guidance throughout has been amazing, he too was always on hand when needed.  
- I would like to thank the [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.

