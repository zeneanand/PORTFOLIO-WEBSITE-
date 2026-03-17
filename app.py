<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Zene Anand | Portfolio</title>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
/* ================= GLOBAL ================= */
* {margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif;}
body {background:#0a0a0a;color:#eaeaea;overflow-x:hidden;}

/* Cursor Glow */
.cursor {
  position: fixed;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, #00F0FF33 0%, transparent 60%);
  pointer-events: none;
  transform: translate(-50%, -50%);
  z-index: 0;
}

/* NAVBAR */
.navbar {
  position: fixed;
  width:100%;
  display:flex;
  justify-content:space-between;
  padding:15px 30px;
  background: rgba(0,0,0,0.7);
  backdrop-filter: blur(10px);
  z-index:1000;
}
.logo {color:#00F0FF;}
.nav-links {display:flex;gap:20px;list-style:none;}
.nav-links a {color:#aaa;text-decoration:none;}
.nav-links a:hover {color:#00F0FF;}

/* Hamburger */
.hamburger {
  display:none;
  flex-direction:column;
  cursor:pointer;
}
.hamburger span {
  height:3px;width:25px;background:white;margin:4px;
}

/* HERO */
.hero {
  height:100vh;
  display:flex;
  align-items:center;
  justify-content:space-around;
  padding:100px 20px;
}
.hero h1 {font-size:3rem;}
.hero h3 {color:#00F0FF;}
.btn {
  background:#00F0FF;color:black;padding:10px 20px;
  text-decoration:none;margin-top:20px;display:inline-block;
}

/* SECTIONS */
.section {padding:80px 20px;text-align:center;}
.img-placeholder {
  border:2px dashed #00F0FF;
  height:200px;display:flex;align-items:center;justify-content:center;
}

/* SKILLS */
.skill {
  margin:15px 0;
}
.bar {
  background:#222;height:8px;border-radius:5px;
}
.progress {
  height:100%;
  width:0;
  background:#00F0FF;
  border-radius:5px;
}

/* PROJECTS */
.project-grid {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:20px;
}
.project-card {
  background:rgba(255,255,255,0.05);
  padding:15px;border-radius:10px;
  transition:0.3s;
}
.project-card:hover {transform:translateY(-10px);}

/* GALLERY */
.gallery {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  gap:15px;
}
.gallery div {
  height:150px;
  background:rgba(255,255,255,0.05);
  border-radius:10px;
}

/* TIMELINE */
.timeline {max-width:600px;margin:auto;}
.timeline-item {
  border-left:2px solid #00F0FF;
  padding-left:10px;margin:20px 0;
}

/* CONTACT */
input, textarea {
  width:80%;padding:10px;margin:10px;
  background:#111;border:none;color:white;
}
button {
  padding:10px 20px;background:#00F0FF;border:none;
}

/* FADE */
.fade {opacity:0;transform:translateY(20px);transition:1s;}
.show {opacity:1;transform:translateY(0);}

/* MOBILE */
@media(max-width:768px){
  .nav-links {
    position:absolute;
    top:60px;right:0;
    background:#111;
    flex-direction:column;
    width:200px;
    display:none;
  }
  .nav-links.active {display:flex;}
  .hamburger {display:flex;}
  .hero {flex-direction:column;text-align:center;}
}
</style>
</head>

<body>

<div class="cursor"></div>

<!-- NAV -->
<header class="navbar">
  <h2 class="logo">Zene.</h2>
  <ul class="nav-links">
    <li><a href="#home">Home</a></li>
    <li><a href="#skills">Skills</a></li>
    <li><a href="#projects">Projects</a></li>
    <li><a href="#gallery">Gallery</a></li>
    <li><a href="#achievements">Achievements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <div class="hamburger">
    <span></span><span></span><span></span>
  </div>
</header>

<!-- HERO -->
<section class="hero" id="home">
  <div>
    <h1>Hi, I'm Zene Anand</h1>
    <h3>AI | Python | Designer</h3>
    <p>Blending intelligence with design & performance.</p>
    <a href="#projects" class="btn">View Work</a>
  </div>
  <div class="img-placeholder">Your Photo</div>
</section>

<!-- SKILLS -->
<section class="section fade" id="skills">
  <h2>Skills</h2>

  <div class="skill">
    <p>Python</p>
    <div class="bar"><div class="progress" data-width="90%"></div></div>
  </div>

  <div class="skill">
    <p>AI</p>
    <div class="bar"><div class="progress" data-width="85%"></div></div>
  </div>

  <div class="skill">
    <p>UI/UX Design</p>
    <div class="bar"><div class="progress" data-width="80%"></div></div>
  </div>

</section>

<!-- PROJECTS -->
<section class="section fade" id="projects">
  <h2>Projects</h2>
  <div class="project-grid">

    <div class="project-card">
      <div class="img-placeholder">Project</div>
      <h3>AI Dashboard</h3>
      <button onclick="openModal()">Live Demo</button>
    </div>

  </div>
</section>

<!-- GALLERY -->
<section class="section fade" id="gallery">
  <h2>Design Gallery</h2>
  <div class="gallery">
    <div></div><div></div><div></div><div></div>
  </div>
</section>

<!-- ACHIEVEMENTS -->
<section class="section fade" id="achievements">
  <h2>Achievements</h2>
  <div class="timeline">
    <div class="timeline-item">UN Geneva Exhibition</div>
    <div class="timeline-item">MUN Distinguished Delegate</div>
    <div class="timeline-item">WhiteHat Jr Developer</div>
  </div>
</section>
<!-- ================= SPORTS ================= -->
<section class="section fade" id="sports">
  <h2>Sports & Discipline</h2>
  <p class="subtitle">Athletics | Football | Basketball</p>

  <div class="sports-grid">

    <div class="sports-card">
      <div class="img-placeholder">Add Photo</div>
      <h3>Best Girl Athlete</h3>
      <p>Aspee Nutan Academy Annual Sports Meet</p>
      <p>Events: 100m, 200m, 4x100m Relay, Basketball, Football</p>
    </div>

    <div class="sports-card">
      <div class="img-placeholder">Add Photo</div>
      <h3>Track Achievements</h3>
      <p><strong>2022–23 (U-14):</strong></p>
      <p>🥇 50m | 🥈 4x100m | 🥉 200m</p>

      <p><strong>2023–24:</strong></p>
      <p>🥈 100m | 🥉 200m | 🥉 Relay | 🥈 Throwball</p>
    </div>

    <div class="sports-card">
      <div class="img-placeholder">Add Photo</div>
      <h3>District & MISA</h3>
      <p>MISA (U-16): 🥉 100m</p>
      <p>Played DSO (District Level)</p>
      <p>Affiliated with MES, Khelo India & FIT India</p>
    </div>

  </div>
</section>
<!-- ================= CASE STUDY ================= -->
<section class="section fade" id="case-study">
  <h2>Case Study</h2>

  <div class="case-block">
    <h3>AI + Design Project</h3>

    <div class="img-placeholder">Project Photo</div>

    <h4>Problem</h4>
    <p>People are unaware of the environmental impact of their purchases.</p>

    <h4>Research</h4>
    <p>Studied consumer behavior and lack of visibility in sustainability metrics.</p>

    <h4>Ideation</h4>
    <p>Designed an AI-powered dashboard to visualize impact in real-time.</p>

    <h4>Solution</h4>
    <p>Built a Python-based system with a clean UI to simplify complex data.</p>

    <h4>Outcome</h4>
    <p>Improved awareness and usability through intuitive design.</p>
  </div>
</section>
/* ================= SPORTS SECTION ================= */
.sports-grid {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:20px;
}

.sports-card {
  background:rgba(255,255,255,0.05);
  padding:20px;
  border-radius:12px;
  transition:0.3s;
}

.sports-card:hover {
  transform:translateY(-10px);
}

<!-- CONTACT -->
<section class="section fade" id="contact">
  <h2>Contact</h2>
  <form id="form">
    <input type="text" placeholder="Name" required>
    <input type="email" placeholder="Email" required>
    <textarea placeholder="Message"></textarea>
    <button type="submit">Send</button>
  </form>
</section>

<!-- MODAL -->
<div id="modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:black;">
  <button onclick="closeModal()">Close</button>
  <p>AI Demo Coming Soon</p>
</div>

<script>
// Cursor glow
document.addEventListener("mousemove", e => {
  document.querySelector(".cursor").style.left = e.clientX + "px";
  document.querySelector(".cursor").style.top = e.clientY + "px";
});

// Hamburger
const ham = document.querySelector(".hamburger");
const nav = document.querySelector(".nav-links");
ham.onclick = () => nav.classList.toggle("active");

// Fade + Skill animation
const elements = document.querySelectorAll(".fade");

window.addEventListener("scroll", () => {
  elements.forEach(el => {
    if(el.getBoundingClientRect().top < window.innerHeight - 100){
      el.classList.add("show");

      el.querySelectorAll(".progress").forEach(bar => {
        bar.style.width = bar.dataset.width;
      });
    }
  });
});

// Modal
function openModal(){document.getElementById("modal").style.display="block";}
function closeModal(){document.getElementById("modal").style.display="none";}

// Form
document.getElementById("form").addEventListener("submit", e=>{
  e.preventDefault();
  alert("Message Sent!");
});
</script>

</body>
</html>
