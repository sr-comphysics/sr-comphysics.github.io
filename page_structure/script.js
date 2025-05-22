// Using the html element for toggling classes
const html = document.documentElement;

// DARK/LIGHT MODE TOGGLE using the modeToggle button
const modeToggle = document.getElementById('modeToggle');
const storedTheme = localStorage.getItem('theme');

if (storedTheme) {
  html.classList.add(storedTheme);
} else {
  // Default theme is dark-mode (already on the HTML element as per your HTML)
  html.classList.add('dark-mode');
}

modeToggle.addEventListener('click', () => {
  // Toggle dark and light mode classes on the html element
  html.classList.toggle('dark-mode');
  html.classList.toggle('light-mode');

  // Save the current theme to local storage
  const currentTheme = html.classList.contains('dark-mode') ? 'dark-mode' : 'light-mode';
  localStorage.setItem('theme', currentTheme);
});

// HIGH CONTRAST TOGGLE
const contrastToggle = document.getElementById('contrastToggle');
contrastToggle.addEventListener('click', () => {
  html.classList.toggle('high-contrast');
});

// HAMBURGER MENU TOGGLE
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

// Toggle mobile menu when hamburger is clicked
hamburger.addEventListener('click', () => {
  const expanded = hamburger.getAttribute('aria-expanded') === 'true';
  hamburger.setAttribute('aria-expanded', !expanded);
  mobileMenu.classList.toggle('show');
});

// Close button inside mobile menu to dismiss the menu
const closeBtn = mobileMenu.querySelector('.close-btn');
if (closeBtn) {
  closeBtn.addEventListener('click', () => {
    mobileMenu.classList.remove('show');
    hamburger.setAttribute('aria-expanded', 'false');
  });
}

// Copy button functionality on tutorial page
document.querySelectorAll('.copy-btn').forEach(button => {
  const copyIconSVG = `
  <svg class="icon-copy" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
  <path d="M10 1H3a2 2 0 0 0-2 2v10h1V3a1 1 0 0 1 1-1h7V1z"/>
  <path d="M13 3H6a2 2 0 0 0-2 2v10a1 1 0 0 0 1 1h7a2 2 0 0 0 2-2V4a1 1 0 0 0-1-1zm0 12H6V5h7v10z"/>
  </svg>`;
  const checkIconSVG = `
  <svg class="icon-check" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#28a745" viewBox="0 0 16 16">
  <path d="M13.485 1.929a.75.75 0 0 1 1.06 1.06L6.53 10.99 3.455 7.915a.75.75 0 1 1 1.06-1.06l1.947 1.947 6.023-6.023z"/>
  </svg>`;

  button.innerHTML = copyIconSVG;

  button.addEventListener('click', () => {
    const codeBlock = button.nextElementSibling;
    if (!codeBlock) return;
    const text = codeBlock.innerText;
    navigator.clipboard.writeText(text).then(() => {
      button.innerHTML = checkIconSVG;
      setTimeout(() => (button.innerHTML = copyIconSVG), 1500);
    }).catch(() => {
      button.style.color = '#d73a49';
      setTimeout(() => {
        button.style.color = '';
        button.innerHTML = copyIconSVG;
      }, 1500);
    });
  });
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

// LANGUAGE TOGGLE
const langBtn = document.getElementById('languageButton');
langBtn.addEventListener('click', () => {
  const currentLang = document.documentElement.lang;
  const targetLang = currentLang === 'en' ? 'ta' : 'en';
  document.documentElement.lang = targetLang;
  localStorage.setItem('lang', targetLang);
  langBtn.textContent = targetLang === 'en' ? 'தமிழ்' : 'English';
  translateContent(targetLang);
});

function translateContent(lang) {
  const translations = {
    en: {

      // Navigation Link
      navLinks: '<a href="#programs">Programs</a><a href="#tutorial">Tutorial</a> <a href="#repository">Repository</a> <a href="#about">About</a> <a href="#contact">Contact</a>',

      // Mobile Navigation
      mobileMenu: '<button class="close-btn" aria-label="Close Menu">×</button> <a href="#programs">Programs</a> <a href="#tutorial">Tutorial</a> <a href="#repository">Repository</a> <a href="#about">About</a> <a href="#contact">Contact</a>',


      // Header Section
      header: '<h1>Welcome to the Computational Physics Hub</h1> <p>Exploring Problem Solving and Data Analysis with Python, GNU Octave, Julia, C, and C++</p>',

      // Programs Section
      programs: '<h2>Programs</h2> <div class="card"> <p>Explore our dedicated directories for problem solving in physics:</p> <ul> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_python" target="_blank">Python Programs</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_c" target="_blank">C Programs</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_cpp" target="_blank">C++ Programs</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_octave" target="_blank">GNU Octave Programs</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_julia" target="_blank">Julia Programs</a></li> </ul> <p>View the entire repository <a href="https://github.com/sr-comphysics/sr-comphysics.github.io" target="_blank">here</a>.</p> </div>',

      // Tutorial Section
      tutorial: '<h2>Tutorial</h2> <div class="card"> <p>Here are tutorials for using the code in this repository...</p> <ul> <li><a href="page/tutorial/tutorial.html">Calculating Pauli Spin Matrix with our Commutator function in GNU Octave</a></li> </ul> </div>',

      // Repository Section
      repoTitle: 'Repository Overview',

      // About Section
      about: '<h2>About This Site</h2> <div class="card"> <p>This site is dedicated to enthusiasts and professionals interested in computational physics, advanced problem solving, and data analysis.</p> </div>',

      // Contact Section
      contact: '<h2>Contact Us</h2> <div class="card"> <p>If you have questions or want to collaborate, get in touch:</p> <ul> <li>Personal: <a href="mailto:sunilsubbarayan10@gmail.com">sunilsubbarayan10@gmail.com</a></li> <li>GitHub Hub: <a href="mailto:comphysics@keemail.me">comphysics@keemail.me</a></li> </ul> </div>',

      // Footer Section
      footer: '<p>&copy; This project is open source and available under the MIT License.</p>',

      t_mainHeading: "Calculating Pauli Spin Matrix with our Commutator function in GNU Octave",
      backHome: "Back to Home"
    },
    ta: {

      // Navigation Link
      navLinks: '<a href="#programs">நிரல்கள்</a><a href="#tutorial">பயிற்சிகள்</a> <a href="#repository">களஞ்சியம்</a> <a href="#about">தளம் பற்றி</a> <a href="#contact">தொடர்பு கொள்ள</a>',

      // Mobile Navigation
      mobileMenu: '<button class="close-btn" aria-label="Close Menu">×</button> <a href="#programs">நிரல்கள்</a> <a href="#tutorial">பயிற்சிகள்</a> <a href="#repository">களஞ்சியம்</a> <a href="#about">தளம் பற்றி</a> <a href="#contact">தொடர்பு கொள்ள</a>',


      header: '<h1>கணக்கீட்டு இயற்பியல் மையத்திற்கு உங்களை வரவேற்கிறோம்</h1> <p>Python, GNU Octave, Julia, C மற்றும் C++ உடன் இயற்பியல் சிக்கல்களுக்கு தீர்வு காணுதல் மற்றும் தரவு பகுப்பாய்வுகள் குறித்து ஆராய்வோம்.',

      // Programs Section
      programs: '<h2>நிரல்கள்</h2> <div class="card"> <p>இயற்பியல் சிக்கல்களை கணினி நிரல்கள் மூலம் தீர்வு காண எங்கள் பிரத்யேக மூலவரைவின் கோபுறைகளை கீழே காணலாம்:</p> <ul> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_python" target="_blank">Python நிரல்கள்</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_c" target="_blank">C நிரல்கள்</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_cpp" target="_blank">C++ நிரல்கள்</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_octave" target="_blank">GNU Octave நிரல்கள்</a></li> <li><a href="https://github.com/sr-comphysics/sr-comphysics.github.io/tree/main/comphysics_julia" target="_blank">Julia நிரல்கள்</a></li> </ul> <p>நிரல்களின் ஒருங்கிணைந்த களஞ்சியத்தை <a href="https://github.com/sr-comphysics/sr-comphysics.github.io" target="_blank">இங்கே காண்க.</a>.</p> </div>',

      // Tutorial Section
      tutorial: '<h2>பயிற்சிகள்</h2> <div class="card"> <p>இந்த களஞ்சியத்தில் உள்ள வரைவுகளை பயன்படுத்துவது குறித்த பயிற்சிகளை இங்கே காணலாம்</p> <ul> <li><a href="page/tutorial/tutorial.html">Calculating Pauli Spin Matrix with our Commutator function in GNU Octave</a></li> </ul> </div>',

      // Repository Section
      repoTitle: 'களஞ்சியம் பற்றிய சிறு விளக்கம்',

      // About Section
      about: '<h2>இந்த தளம் பற்றி</h2> <div class="card"> <p>இந்த பக்கம், கணக்கீட்டு இயற்பியல், மேம்பட்ட சிக்கல் தீர்க்கும் திறன் மற்றும் தரவு பகுப்பாய்வு ஆகியவற்றில் ஆர்வமுள்ள ஆர்வலர்கள் மற்றும் வல்லுனர்களுக்காக அர்ப்பணிக்கப்பட்டது.</p> </div>',

      // Contact Section
      contact: '<h2>எங்களைத் தொடர்பு கொள்ள</h2> <div class="card"> <p>உங்களுக்கு எதேனும் கேள்விகள், சந்தேகங்கள் இருந்தாலோ அல்லது எங்களுடன் இணைந்து செயல்பட விரும்பினாலோ, கீழ்காணும் மின்னஞ்சல்கள் மூலம் எங்களை அணுகலாம்.</p> <ul> <li>தனிப்பட்ட முகவரி: <a href="mailto:sunilsubbarayan10@gmail.com">sunilsubbarayan10@gmail.com</a></li> <li>பொது முகவரி: <a href="mailto:comphysics@keemail.me">comphysics@keemail.me</a></li> </ul> </div>',

      // Footer Section
      footer: '<p>&copy; MIT திறமூல மென்பொருள் அனுமதியின்  கீழ் உரிமம் பெற்றது.</p>',

      t_mainHeading: "Pauli Spin Matrix ஐ Commutator செயலாற்றி GNU Octave-ல் கணக்கிடுவது",
      backHome: "முகப்புக்கு திரும்ப"
    }
  };

  const t = translations[lang];
  const keys = Object.keys(t);

  keys.forEach(key => {
    const el = document.getElementById(key);
    if (el) el.innerHTML = t[key];  // Use innerHTML to preserve formatting
  });
}

// Load saved language or default to 'en'
const savedLang = localStorage.getItem('lang') || 'en';
document.documentElement.lang = savedLang;
translateContent(savedLang);
langBtn.textContent = savedLang === 'en' ? 'தமிழ்' : 'English';

// SCREEN READER SHORTCUT (if you have a button configured for this)
const screenReaderBtn = document.getElementById('screenReaderToggle');
if (screenReaderBtn) {
  screenReaderBtn.addEventListener('click', () => {
    alert('Screen reader mode enabled. Use tab and arrow keys to navigate.');
  });
}
