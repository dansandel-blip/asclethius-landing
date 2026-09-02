from pathlib import Path
import re

path = Path("index.html")
html = path.read_text(encoding="utf-8")

# Safe to run more than once.
if 'id="investment"' in html and 'class="contact-form"' in html and 'class="case-live-card reveal"' in html:
    print("Asclethius production refinements already applied.")
    raise SystemExit(0)

EXTRA_CSS = r'''

/* Production launch refinements */
.brand-lockup{display:flex;flex-direction:column;align-items:flex-start;gap:4px;letter-spacing:0}
.brand-lockup>span{font-family:Cinzel,serif;letter-spacing:.15em;font-size:17px;line-height:1}
.brand-lockup sup,.footer-brand sup{font-family:Inter,sans-serif;font-size:.42em;letter-spacing:0;vertical-align:top;margin-left:2px}
.brand-lockup small{font-family:Inter,sans-serif;font-size:8px;font-weight:400;letter-spacing:.035em;color:var(--mut2);line-height:1.2}

.investment-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.investment-card{position:relative;padding:30px;border:1px solid var(--line);border-radius:22px;background:linear-gradient(150deg,rgba(255,255,255,.04),rgba(255,255,255,.015));overflow:hidden}
.investment-card::after{content:"";position:absolute;width:190px;height:190px;border-radius:50%;right:-95px;bottom:-110px;background:radial-gradient(circle,rgba(34,211,238,.08),transparent 68%)}
.investment-card:nth-child(even)::after{background:radial-gradient(circle,rgba(139,92,246,.09),transparent 68%)}
.investment-kicker{color:var(--mut2);font-size:10px;letter-spacing:.14em;text-transform:uppercase}
.investment-card h3{font-family:Cinzel,serif;font-size:23px;font-weight:500;line-height:1.25;margin:28px 0 10px}
.investment-price{font-family:Cinzel,serif;font-size:31px;line-height:1.1;margin-bottom:16px;background:linear-gradient(95deg,#fff,#81eaff,#baa6ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.investment-card p{color:var(--mut);font-size:13px;line-height:1.65;margin:0}
.investment-note{color:var(--mut2);font-size:12px;line-height:1.65;margin:24px 0 0}

.case-live-card{position:relative;min-height:460px;border:1px solid var(--line);border-radius:28px;overflow:hidden;background:radial-gradient(700px 420px at 78% 18%,rgba(34,211,238,.12),transparent 62%),radial-gradient(600px 420px at 8% 88%,rgba(139,92,246,.13),transparent 66%),linear-gradient(150deg,rgba(16,20,34,.84),rgba(7,9,15,.94));box-shadow:0 45px 120px rgba(0,0,0,.38);display:grid;grid-template-rows:auto 1fr auto;transition:transform .2s ease,border-color .2s ease}
.case-live-card:hover{transform:translateY(-4px);border-color:rgba(255,255,255,.22)}
.case-live-header{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:22px 26px;border-bottom:1px solid rgba(255,255,255,.08);color:var(--mut2);font-size:9px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.case-live-header span:last-child{color:rgba(197,247,255,.76)}
.case-live-body{padding:38px 42px 34px;display:flex;flex-direction:column;justify-content:center}
.case-live-kicker{color:var(--mut2);font-size:10px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:18px}
.case-live-brand{font-family:Cinzel,serif;font-size:clamp(30px,3.4vw,46px);font-weight:500;letter-spacing:-.015em;line-height:1.08;margin-bottom:12px}
.case-live-meta{font-size:12px;color:rgba(235,240,255,.56);letter-spacing:.06em;margin-bottom:24px}
.case-live-card p{max-width:560px;margin:0 0 26px;color:var(--mut);font-size:14px;line-height:1.7}
.case-live-tags{display:flex;gap:8px;flex-wrap:wrap}
.case-live-tags span{padding:8px 10px;border:1px solid rgba(255,255,255,.09);border-radius:999px;background:rgba(255,255,255,.025);color:rgba(235,240,255,.66);font-size:10px;letter-spacing:.04em}
.case-live-footer{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:20px 26px;border-top:1px solid rgba(255,255,255,.08);font-size:12px}
.case-live-footer span{color:var(--mut2)}
.case-live-footer strong{font-weight:600;color:#a8f3ff}

.contact-form{max-width:900px;margin:36px auto 26px;display:grid;grid-template-columns:1fr 1fr;gap:14px;text-align:left}
.form-field{display:grid;gap:8px}
.form-field.full{grid-column:1/-1}
.form-field label{color:rgba(242,245,255,.72);font-size:11px;text-transform:uppercase;letter-spacing:.10em}
.form-field input,.form-field select,.form-field textarea{width:100%;border:1px solid var(--line2);border-radius:13px;background:rgba(0,0,0,.24);color:#fff;padding:14px 15px;font:inherit;font-size:14px;outline:none;transition:border-color .18s ease,box-shadow .18s ease,background .18s ease}
.form-field input,.form-field select{height:51px}
.form-field textarea{min-height:145px;resize:vertical;line-height:1.5}
.form-field input:focus,.form-field select:focus,.form-field textarea:focus{border-color:rgba(34,211,238,.48);box-shadow:0 0 0 5px rgba(34,211,238,.07);background:rgba(0,0,0,.32)}
.form-field select option{background:#0b0d14;color:#fff}
.form-actions{grid-column:1/-1;display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-top:4px}
.form-actions button{cursor:pointer;font-family:inherit;color:#fff}
.form-privacy{color:var(--mut2);font-size:11px;line-height:1.55;max-width:520px}
.form-success{max-width:760px;margin:38px auto 0;padding:28px;border:1px solid rgba(34,211,238,.20);border-radius:18px;background:rgba(34,211,238,.05);text-align:center}
.form-success h3{font-family:Cinzel,serif;font-weight:500;margin:0 0 10px}
.form-success p{margin:0 auto;color:var(--mut);font-size:13px}
.footer-sub{font-family:Inter,sans-serif;letter-spacing:.035em}

@media(max-width:760px){
  .investment-grid,.contact-form{grid-template-columns:1fr}
  .form-field.full,.form-actions{grid-column:auto}
  .case-live-card{min-height:390px}
  .case-live-body{padding:30px}
  .case-live-header,.case-live-footer{padding-left:22px;padding-right:22px}
  .case-live-header span:last-child{display:none}
  .brand-lockup small{display:none}
}
'''

html = html.replace("</style>", EXTRA_CSS + "\n</style>", 1)

old_brand = '<a class="brand" href="#top" aria-label="Asclethius home">ASCLETHIUS</a>'
new_brand = '''<a class="brand brand-lockup" href="#top" aria-label="Asclethius home">
        <span>ASCLETHIUS<sup>™</sup></span>
        <small>Practice design for modern medicine.</small>
      </a>'''
if old_brand not in html:
    raise RuntimeError("Header brand marker not found")
html = html.replace(old_brand, new_brand, 1)

nav_marker = '        <a class="nav-cta" href="#contact">Build your practice</a>'
if nav_marker in html and 'href="#investment"' not in html:
    html = html.replace(nav_marker, '        <a href="#investment">Investment</a>\n' + nav_marker, 1)

case_panel = r'''<a class="case-live-card reveal" href="https://sandelduggal.com/" target="_blank" rel="noopener" aria-label="View the Sandel Duggal website">
          <div class="case-live-header"><span>Case Study 01</span><span>Plastic Surgery + Med Spa</span></div>
          <div class="case-live-body">
            <div class="case-live-kicker">Flagship implementation</div>
            <div class="case-live-brand">Sandel Duggal Plastic Surgery</div>
            <div class="case-live-meta">Annapolis, Maryland</div>
            <p>A complete practice experience bringing brand, content, patient navigation, search architecture and technology into one coherent system.</p>
            <div class="case-live-tags"><span>Brand system</span><span>Digital experience</span><span>Patient navigation</span><span>Search architecture</span><span>Practice technology</span></div>
          </div>
          <div class="case-live-footer"><span>sandelduggal.com</span><strong>View the live work <span aria-hidden="true">↗</span></strong></div>
        </a>'''
html, n = re.subn(
    r'<a class="browser reveal" href="https://sandelduggal\.com/"[\s\S]*?</a>',
    case_panel,
    html,
    count=1,
)
if n != 1:
    raise RuntimeError(f"Expected one Sandel Duggal mock panel, replaced {n}")

pricing = r'''
    <section class="section" id="investment">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-label">06 / Typical investment</div>
          <div>
            <h2 class="section-title">Clear enough to plan. Flexible enough to fit the practice.</h2>
            <p class="section-copy">Every engagement is scoped around what already exists, what should be preserved and what actually needs to change. These ranges are intended to establish realistic budget expectations before a conversation begins.</p>
          </div>
        </div>
        <div class="investment-grid">
          <article class="investment-card reveal">
            <div class="investment-kicker">Focused engagement</div>
            <h3>Practice Upgrade</h3>
            <div class="investment-price">$5k–$12k</div>
            <p>A targeted rebrand, patient-material system, digital experience improvement, search project or other defined practice problem.</p>
          </article>
          <article class="investment-card reveal">
            <div class="investment-kicker">Digital flagship</div>
            <h3>Signature Website</h3>
            <div class="investment-price">$25k–$60k</div>
            <p>Custom website strategy, architecture, design and build with migration planning, search preservation, analytics and key practice integrations.</p>
          </article>
          <article class="investment-card reveal">
            <div class="investment-kicker">Integrated transformation</div>
            <h3>Brand + Digital</h3>
            <div class="investment-price">$25k–$45k</div>
            <p>Practice positioning and identity integrated with a new digital experience and a coordinated system of core patient-facing materials.</p>
          </article>
          <article class="investment-card reveal">
            <div class="investment-kicker">End-to-end system</div>
            <h3>Complete Practice Transformation</h3>
            <div class="investment-price">$40k–$75k+</div>
            <p>Brand, website, patient experience, communications, search intelligence, analytics and selected automation designed as one practice system.</p>
          </article>
        </div>
        <p class="investment-note">Ongoing search, analytics, content, optimization and automation support can be added where useful. Final scope and investment are established after an initial practice review.</p>
      </div>
    </section>
'''
initial_focus = '''    <section class="section section-tight">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-label">06 / Initial focus</div>'''
if initial_focus not in html:
    raise RuntimeError("Initial focus marker not found")
html = html.replace(initial_focus, pricing + "\n" + initial_focus.replace("06 / Initial focus", "07 / Initial focus"), 1)

contact = r'''    <section class="section" id="contact">
      <div class="container">
        <div class="cta reveal">
          <div class="eyebrow">Practice design for modern medicine</div>
          <h2>Build the practice patients expect you to be.</h2>
          <p>Whether the starting point is a website, a rebrand, patient-facing materials or a complete practice transformation, Asclethius can design the pieces as one system.</p>
          <form class="contact-form" action="https://formsubmit.co/dansandel@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="New Asclethius practice inquiry">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_next" value="https://www.asclethius.com/?submitted=1#contact">
            <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
            <div class="form-field">
              <label for="as-name">Name</label>
              <input id="as-name" name="name" type="text" autocomplete="name" required>
            </div>
            <div class="form-field">
              <label for="as-email">Email</label>
              <input id="as-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="form-field">
              <label for="as-practice">Practice / organization</label>
              <input id="as-practice" name="practice" type="text" autocomplete="organization" required>
            </div>
            <div class="form-field">
              <label for="as-site">Current website <span style="text-transform:none;letter-spacing:0;opacity:.6">(optional)</span></label>
              <input id="as-site" name="website" type="url" inputmode="url" placeholder="https://">
            </div>
            <div class="form-field full">
              <label for="as-interest">What are you considering?</label>
              <select id="as-interest" name="project_interest" required>
                <option value="" selected disabled>Select an area</option>
                <option>Website & digital experience</option>
                <option>Brand or practice rebrand</option>
                <option>Patient-facing materials & communications</option>
                <option>Search, content & analytics</option>
                <option>AI & practice automation</option>
                <option>Complete practice transformation</option>
                <option>Not sure yet</option>
              </select>
            </div>
            <div class="form-field full">
              <label for="as-message">Tell us about the practice and what you want to improve</label>
              <textarea id="as-message" name="message" required></textarea>
            </div>
            <div class="form-actions">
              <button class="btn btn-primary" type="submit">Begin a conversation <span aria-hidden="true">→</span></button>
              <div class="form-privacy">For practice and professional inquiries only. Please do not submit patient information or protected health information.</div>
            </div>
          </form>
          <p class="contact-note">Inquiries are delivered directly to Asclethius. Please do not include patient information.</p>
        </div>
      </div>
    </section>'''
html, n = re.subn(
    r'    <section class="section" id="contact">[\s\S]*?    </section>',
    contact,
    html,
    count=1,
)
if n != 1:
    raise RuntimeError(f"Expected one contact section, replaced {n}")

old_footer = '''      <div>
        <div class="footer-brand">ASCLETHIUS</div>
        <div class="footer-sub">Ancient wisdom. Modern precision.</div>
      </div>'''
new_footer = '''      <div class="footer-lockup">
        <div class="footer-brand">ASCLETHIUS<sup>™</sup></div>
        <div class="footer-sub">Practice design for modern medicine.</div>
      </div>'''
if old_footer not in html:
    raise RuntimeError("Footer brand marker not found")
html = html.replace(old_footer, new_footer, 1)

SUCCESS_JS = r'''
<script>
(function(){
  const params = new URLSearchParams(window.location.search);
  if(params.get('submitted') === '1'){
    const form = document.querySelector('.contact-form');
    if(form){
      const success = document.createElement('div');
      success.className = 'form-success';
      success.innerHTML = '<h3>Thank you.</h3><p>Your inquiry has been received. We’ll be in touch.</p>';
      form.replaceWith(success);
    }
  }
})();
</script>
'''
html = html.replace("</body>", SUCCESS_JS + "\n</body>", 1)

path.write_text(html, encoding="utf-8")
print("Applied Asclethius production launch refinements.")
