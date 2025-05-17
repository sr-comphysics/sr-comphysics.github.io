// Toggle navigation menu on mobile when hamburger is clicked.
const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");
hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});

// Load repository README content using marked.js
const readmeUrl = "https://raw.githubusercontent.com/sr-comphysics/sr-comphysics.github.io/main/README.md";
fetch(readmeUrl)
.then((response) => {
    if (!response.ok) {
        throw new Error("Network response was not ok: " + response.statusText);
    }
    return response.text();
})
.then((markdown) => {
    document.getElementById("readme").innerHTML = marked.parse(markdown);
})
.catch((error) => {
    document.getElementById("readme").innerHTML =
    "Failed to load README content: " + error.message;
});

let currentLanguage = "en";

function toggleLanguage() {
    if (currentLanguage === "en") {

        // Tamil Translation

        // Accessibility Section
        document.getElementById("screenReader").innerHTML = "திரை வாசகர";
        document.getElementById("contrastButton").innerHTML = "உயர் மாறுபாடு";

        // Header Section
        document.getElementById("mainHeading").innerText = "கணக்கீட்டு இயற்பியல் மையத்திற்கு உங்களை வரவேற்கிறோம்";
        document.getElementById("subHeading").innerText ="Python, GNU Octave, Julia, C மற்றும் C++ உடன் இயற்பியல் சிக்கல்களுக்கு தீர்வு காணுதல் மற்றும் தரவு பகுப்பாய்வுகள் குறித்து ஆராய்வோம்.";

        // About Section
        document.getElementById("about-title").innerText = "இந்த தளம் பற்றி";
        document.getElementById("about-text").innerText =
        "இந்த பக்கம், கணக்கீட்டு இயற்பியல், மேம்பட்ட சிக்கல் தீர்க்கும் திறன் மற்றும் தரவு பகுப்பாய்வு ஆகியவற்றில் ஆர்வமுள்ள ஆர்வலர்கள் மற்றும் வல்லுனர்களுக்காக அர்ப்பணிக்கப்பட்டது.";

        // Programs Section
        document.getElementById("program-title").innerText = "நிரல்கள்";
        document.getElementById("programs-text").innerText =
        "இயற்பியல் சிக்கல்களை கணினி நிரல்கள் மூலம் தீர்வு காண எங்கள் பிரத்யேக மூலவரைவின் கோபுறைகளை கீழே காணலாம்:";
        document.getElementById("programs-list").innerHTML = `<li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_python" target="_blank">Python நிரல்கள்</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_c" target="_blank">C நிரல்கள்</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_cpp" target="_blank">C++ நிரல்கள்</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_octave" target="_blank">GNU Octave நிரல்கள்</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_julia" target="_blank">Julia நிரல்கள்</a></li>`;
        document.getElementById("repo-link").innerHTML =
        'நிரல்களின் ஒருங்கிணைந்த களஞ்சியத்தை <a href="https://github.com/sr-comphysics/sr-comphysics.github.io" target="_blank">இங்கே காண்க.</a>';

        // Repository Overview Section
        document.getElementById("repo-title").innerText = "களஞ்சியம் பற்றிய சிறு விளக்கம்";

        // Contact Section
        document.getElementById("contact-title").innerText = "எங்களை தொடர்பு கொள்ள";
        document.getElementById("contact-text").innerText =
        "உங்களுக்கு எதேனும் கேள்விகள், சந்தேகங்கள் இருந்தாலோ அல்லது எங்களுடன் இணைந்து செயல்பட விரும்பினாலோ, கீழ்காணும் மின்னஞ்சல்கள் மூலம் எங்களை அணுகலாம்.";
        document.getElementById("contact-list").innerHTML = `<li>தனிப்பட்ட முகவரி: <a href="mailto:sunilsubbarayan10@gmail.com">sunilsubbarayan10@gmail.com</a></li>
        <li>பொது முகவரி: <a href="mailto:comphysics@keemail.me">comphysics@keemail.me</a></li>`;

        document.getElementById("nav-links").innerHTML = `<li><a href="#">முகப்பு</a></li>
        <li><a href="#programs">நிரல்கள்</a></li>
        <li><a href="#repo-readme">களஞ்சியம்</a></li>
        <li><a href="#about">தளம் பற்றி</a></li>
        <li><a href="#contact">தொடர்பு கொள்ள</a></li>`;

        document.getElementById("mobileMenu").innerHTML = `<button class="close-btn" onclick="toggleMobileMenu()">x</button>
        <a href="#home" onclick="toggleMobileMenu()">முகப்பு</a>
        <a href="#programs" onclick="toggleMobileMenu()">நிரல்கள்</a>
        <a href="#repo-readme" onclick="toggleMobileMenu()">களஞ்சியம்</a>
        <a href="#about" onclick="toggleMobileMenu()">தளம் பற்றி</a>
        <a href="#contact" onclick="toggleMobileMenu()">தொடர்பு கொள்ள</a>`;

        // Footer Section
        document.getElementById("footer-text").innerHTML = '&copy; MIT திறமூல மென்பொருள் அனுமதியின்  கீழ் உரிமம் பெற்றது.';

        // Language button to allow switching back to English
        document.getElementById("languageButton").innerText = "English";
        currentLanguage = "ta";
    } else {

        // English Translations
        //  Accessibility Section
        document.getElementById("screenReader").innerHTML = "Screen Reader";
        document.getElementById("contrastButton").innerHTML = "High Contrast";

        // Header Section
        document.getElementById("mainHeading").innerText = "Welcome to the Computational Physics Hub";
        document.getElementById("subHeading").innerText = "Exploring Problem Solving and Data Analysis with Python, GNU Octave, Julia, C, and C++";

        // About Section
        document.getElementById("about-title").innerText = "About This Site";
        document.getElementById("about-text").innerText =
        "This site is dedicated to enthusiasts and professionals interested in computational physics, advanced problem solving, and data analysis.";

        // Programs Section
        document.getElementById("program-title").innerText = "Programs";
        document.getElementById("programs-text").innerText =
        "Explore our dedicated directories for problem solving in physics:";
        document.getElementById("programs-list").innerHTML = `<li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_python" target="_blank">Python Programs</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_c" target="_blank">C Programs</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_cpp" target="_blank">C++ Programs</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_octave" target="_blank">GNU Octave Programs</a></li>
        <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_julia" target="_blank">Julia Programs</a></li>`;
        document.getElementById("repo-link").innerHTML =
        'View the entire repository <a href="https://github.com/sr-comphysics/sr-comphysics.github.io" target="_blank">here</a>.';

        // Repository Overview Section
        document.getElementById("repo-title").innerText = "Repository Overview";

        // Contact Section
        document.getElementById("contact-title").innerText = "Contact Us";
        document.getElementById("contact-text").innerText =
        "If you have questions or want to collaborate, get in touch:";
        document.getElementById("contact-list").innerHTML = `<li>Personal: <a href="mailto:sunilsubbarayan10@gmail.com">sunilsubbarayan10@gmail.com</a></li>
        <li>GitHub Hub: <a href="mailto:comphysics@keemail.com">comphysics@keemail.com</a></li>`;


        document.getElementById("nav-links").innerHTML = `<li><a href="#">Home</a></li>
        <li><a href="#programs">Programs</a></li>
        <li><a href="#repo-readme">Repository</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#contact">Contact</a></li>`;

        document.getElementById("mobileMenu").innerHTML = `<button class="close-btn" onclick="toggleMobileMenu()">x</button>
        <a href="#home" onclick="toggleMobileMenu()">Home</a>
        <a href="#programs" onclick="toggleMobileMenu()">Programs</a>
        <a href="#repo-readme" onclick="toggleMobileMenu()">Repository</a>
        <a href="#about" onclick="toggleMobileMenu()">About</a>
        <a href="#contact" onclick="toggleMobileMenu()">Contact</a>`;

        // Footer Section
        document.getElementById("footer-text").innerHTML = "&copy; This project is open source and available under the MIT License.";

        // Language button to allow switching to Tamil.
        document.getElementById("languageButton").innerText = "தமிழ்";
        currentLanguage = "en";
    }
    console.log("Current Language: " + currentLanguage);
}

// Accessibility Functions
function toggleMobileMenu() {
    document.getElementById('mobileMenu').classList.toggle('show');
}

function activateScreenReader() {
    alert(
        "Screen reader functionality is handled by your device/browser. Please ensure your assistive technology is enabled."
    );
    console.log("Screen reader activated (placeholder)");
}

function toggleHighContrast() {
    document.body.classList.toggle("high-contrast");
    const contrastButton = document.getElementById("contrastButton");
    if (document.body.classList.contains("high-contrast")) {
        contrastButton.innerText = "Normal Mode";
    } else {
        contrastButton.innerText = "High Contrast";
    }
    console.log("High contrast mode toggled.");
}
