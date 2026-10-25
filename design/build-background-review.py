from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / 'index.html').read_text()
page = page.replace('<head>', '<head>\n  <base href="../">')
page = page.replace('<script src="assets/js/theme.js"></script>', '''<script>
document.documentElement.dataset.theme = new URLSearchParams(location.search).get('theme') === 'dark' ? 'dark' : 'light';
</script>''')
page = page.replace('</head>', '''<style>
body { position:relative; isolation:isolate; min-height:100vh; }
.math-background { position:absolute; inset:0; overflow:hidden; z-index:-1; pointer-events:none; color:#45665f; }
.math-background svg { width:100%; height:100%; min-height:1100px; position:absolute; inset:0; }
.math-background .pencil { fill:none; stroke:currentColor; stroke-width:1.1; stroke-linecap:round; stroke-linejoin:round; opacity:.19; }
.math-background .echo { opacity:.085; stroke-width:.6; }
.math-background .annotation { font:italic 18px Georgia,serif; fill:currentColor; opacity:.25; }
.math-background .small { font-size:14px; }
.math-background .wash { fill:currentColor; opacity:.026; }
.math-background .point { fill:currentColor; opacity:.28; }
.quote p { color:var(--ink); }
.review-mode { width:34px; height:34px; display:grid; place-items:center; border:1px solid var(--line); border-radius:50%; color:var(--ink); font-size:18px; }
html[data-theme=dark] .math-background { color:#88a8a5; }
html[data-theme=dark] .math-background .pencil { opacity:.17; }
html[data-theme=dark] .math-background .annotation { opacity:.23; }
html[data-theme=dark] .math-background .wash { opacity:.032; }
@media(max-width:720px) { .math-background svg { width:1100px; left:50%; transform:translateX(-50%); opacity:.55; } }
</style></head>''')
page = page.replace('</nav>', '</nav><a class="review-mode" href="design/background-review.html?theme=dark" aria-label="Preview dark mode">◐</a>')
page = page.replace('<body>', '''<body>
<div class="math-background" aria-hidden="true">
<svg viewBox="0 0 1440 1150" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<defs>
 <marker id="pencil-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M1 1L8 5 1 9" fill="none" stroke="currentColor" stroke-width="1.3"/></marker>
 <linearGradient id="content-fade"><stop offset="0" stop-color="white"/><stop offset=".085" stop-color="white"/><stop offset=".14" stop-color="#111"/><stop offset=".23" stop-color="black"/><stop offset=".77" stop-color="black"/><stop offset=".86" stop-color="#111"/><stop offset=".915" stop-color="white"/><stop offset="1" stop-color="white"/></linearGradient>
 <mask id="quiet-center"><rect width="1440" height="1150" fill="url(#content-fade)"/></mask>
</defs>
<g mask="url(#quiet-center)">
 <!-- Quadratic level sets, with a path entering successively lower levels. -->
 <g transform="translate(68 190) rotate(-28)">
  <g class="pencil">
   <ellipse rx="35" ry="57"/><ellipse rx="62" ry="101"/><ellipse rx="94" ry="145"/><ellipse rx="133" ry="194"/><ellipse rx="176" ry="249"/><ellipse rx="218" ry="309"/>
  </g>
  <g class="pencil echo" transform="translate(1.6 -1.1) rotate(.4)">
   <ellipse rx="62" ry="101"/><ellipse rx="133" ry="194"/><ellipse rx="218" ry="309"/>
  </g>
 </g>
 <path class="pencil" d="M-12 13 C10 49 35 73 39 104 S80 129 84 155 S68 176 68 189" stroke-dasharray="3 6"/>
 <path class="pencil" d="M38 98 Q63 112 72 137" marker-end="url(#pencil-arrow)"/>
 <circle class="point" cx="38" cy="98" r="2.6"/><circle class="point" cx="68" cy="189" r="2.2"/>
 <text class="annotation" x="73" y="105" transform="rotate(-10 73 105)">−∇f(x)</text>
 <text class="annotation small" x="94" y="309" transform="rotate(-15 94 309)">f(x) = c</text>
 <!-- A normal cone at a convex corner: normals span the outward sector. -->
 <g transform="translate(1320 438) scale(.72) rotate(-7)">
  <path class="wash" d="M0 0L63-114Q117-64 129 8Z"/>
  <path class="wash" d="M0 0L-91-61Q-160 43-59 125L-5 95Z"/>
  <path class="pencil" d="M-110-74 Q-50-45 0 0Q-7 55-7 103"/>
  <path class="pencil echo" d="M-112-75 Q-49-43 1 1Q-5 54-6 103"/>
  <path class="pencil" d="M0 0L63-114M0 0L129 8"/>
  <path class="pencil" d="M0 0L98-66" marker-end="url(#pencil-arrow)"/>
  <path class="pencil" d="M23-41Q49-29 48 3" stroke-dasharray="3 5"/>
  <circle class="point" r="3"/>
  <text class="annotation" x="50" y="-127">N<tspan baseline-shift="sub" font-size="12">C</tspan>(x)</text>
  <text class="annotation small" x="-22" y="23">x</text>
  <text class="annotation small" x="-74" y="49">C</text>
 </g>
 <!-- The polar of a linearized feasible cone, sketched from two active gradients. -->
 <g transform="translate(68 831) scale(.72) rotate(8)">
  <path class="wash" d="M0 0L109-57Q121-9 104 47Z"/>
  <path class="pencil" d="M-73-144L71 141M-66 143L63-134" stroke-dasharray="4 6"/>
  <path class="pencil" d="M-79-138Q-31-68 0 0T48 151M-83 140Q-44 64 0 0T83-127"/>
  <path class="pencil echo" d="M-81-139Q-29-67 1 0T50 150"/>
  <path class="pencil" d="M0 0L109-57M0 0L104 47" marker-end="url(#pencil-arrow)"/>
  <path class="pencil" d="M35-18Q43-1 34 16"/>
  <circle class="point" r="3"/>
  <text class="annotation" x="54" y="-79">N<tspan baseline-shift="sub" font-size="12">lin</tspan>(x)</text>
  <text class="annotation small" x="82" y="-34">∇g₁</text>
  <text class="annotation small" x="80" y="70">∇g₂</text>
  <text class="annotation small" x="-22" y="27">x</text>
 </g>
 <!-- A few receding level curves close the composition at the foot of the page. -->
 <g class="pencil" transform="translate(1440 1140) rotate(-35)">
  <ellipse rx="122" ry="72"/><ellipse rx="187" ry="110"/><ellipse rx="257" ry="153"/><ellipse rx="333" ry="199"/>
 </g>
</g></svg></div>''')
page = page.replace('</body>', '''<script>
const modeLink = document.querySelector('.review-mode');
if (document.documentElement.dataset.theme === 'dark') {
 modeLink.href = 'design/background-review.html?theme=light';
 modeLink.setAttribute('aria-label','Preview light mode');
}
</script></body>''')
(root / 'design/background-review.html').write_text(page)
