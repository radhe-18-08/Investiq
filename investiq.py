import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="InvestIQ",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI chrome
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100%;}
    .stApp {background: #04120a;}
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>InvestIQ</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#04120a;display:flex;justify-content:center;padding:20px;min-height:100vh}

/* ── PHONE SHELL ── */
.phone{width:390px;border-radius:42px;border:2px solid #1a3a24;background:#071a0e;overflow:hidden;display:flex;flex-direction:column;min-height:780px}
.screen{display:none;flex-direction:column;flex:1}
.screen.active{display:flex}
.sb{background:#071a0e;display:flex;justify-content:space-between;padding:12px 24px 6px;font-size:11px;color:#3a6647;flex-shrink:0}

/* ── INPUTS ── */
.inp{width:100%;background:#0a2214;border:1.5px solid #1a3a24;border-radius:12px;padding:13px 16px;font-size:14px;color:#e0f0e6;outline:none;transition:border-color .2s}
.inp:focus{border-color:#2ecc71}
.inp::placeholder{color:#1e4a2c}
.inp-label{font-size:12px;color:#5a8a6a;margin-bottom:6px}
.inp-wrap{margin-bottom:16px}
.btn-primary{width:100%;background:#2ecc71;color:#03100a;border:none;border-radius:12px;padding:14px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;letter-spacing:.3px}
.btn-primary:hover{background:#27ae60}
.btn-primary:active{transform:scale(.98)}
.link-row{text-align:center;margin-top:18px;font-size:13px;color:#3a6647}
.link-row a{color:#2ecc71;cursor:pointer;text-decoration:none}
.err{font-size:12px;color:#e74c3c;margin-top:-10px;margin-bottom:12px;display:none}
.hint{text-align:center;font-size:11px;color:#1e4a2c;margin-top:20px}

/* ── LOGIN ── */
.login-body{flex:1;display:flex;flex-direction:column;justify-content:center;padding:36px 28px;background:#071a0e}
.brand{text-align:center;margin-bottom:40px}
.brand-name{font-size:34px;font-weight:700;color:#e0f0e6;letter-spacing:.5px}
.brand-name span{color:#2ecc71}
.brand-tag{font-size:13px;color:#3a6647;margin-top:8px}
.brand-dot{width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;margin-bottom:16px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.6;transform:scale(.8)}}
@keyframes spin{to{transform:rotate(360deg)}}

/* ── SIGNUP ── */
.signup-body{flex:1;display:flex;flex-direction:column;padding:26px 28px;background:#071a0e;overflow-y:auto}
.back-link{color:#2ecc71;font-size:13px;cursor:pointer;margin-bottom:18px}
.signup-title{font-size:22px;font-weight:700;color:#e0f0e6;margin-bottom:6px}
.signup-sub{font-size:13px;color:#3a6647;margin-bottom:22px}
.row-2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cb-row{display:flex;gap:10px;align-items:flex-start;margin-bottom:20px}
.cb-row label{font-size:12px;color:#3a6647;line-height:1.6}
.cb-row a{color:#2ecc71}

/* ── APP CHROME ── */
.app-header{background:#071a0e;padding:13px 20px 11px;display:flex;justify-content:space-between;align-items:center;flex-shrink:0;border-bottom:1px solid #0f2a18}
.app-logo{font-size:17px;font-weight:700;color:#e0f0e6}
.app-logo span{color:#2ecc71}
.hdr-right{display:flex;gap:10px;align-items:center}
.icon-btn{width:34px;height:34px;border-radius:50%;background:#0a2214;display:flex;align-items:center;justify-content:center;cursor:pointer;border:1px solid #1a3a24;position:relative}
.badge{width:8px;height:8px;background:#2ecc71;border-radius:50%;position:absolute;top:5px;right:5px;border:1.5px solid #071a0e}
.avatar{width:34px;height:34px;border-radius:50%;background:#0f3a1e;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#2ecc71;cursor:pointer;border:1px solid #1a5a2c}

/* ── TABS ── */
.tabs{display:flex;background:#071a0e;border-bottom:1px solid #0f2a18;flex-shrink:0;overflow-x:auto}
.tabs::-webkit-scrollbar{height:0}
.tab{flex:1;min-width:68px;padding:11px 4px;font-size:11px;color:#3a6647;text-align:center;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .2s}
.tab.active{color:#2ecc71;border-bottom-color:#2ecc71}

/* ── SCROLL ── */
.scroll{flex:1;overflow-y:auto;background:#04120a}
.scroll::-webkit-scrollbar{width:0}

/* ── COLOURS ── */
.pos{color:#2ecc71}
.neg{color:#e74c3c}
.neutral{color:#3a6647}
.warn{color:#f39c12}

/* ── CARDS ── */
.stat-card{background:#071a0e;border-radius:12px;padding:13px 15px;border:1px solid #0f2a18}
.sc-label{font-size:10px;color:#3a6647;margin-bottom:5px;text-transform:uppercase;letter-spacing:.4px}
.sc-val{font-size:19px;font-weight:700;color:#e0f0e6}
.sc-sub{font-size:11px;margin-top:3px}
.cards-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:16px}

/* ── HERO ── */
.hero{background:#071a0e;padding:16px 20px 20px;border-bottom:1px solid #0f2a18}
.hero-greeting{font-size:12px;color:#3a6647;margin-bottom:10px}
.hero-label{font-size:11px;color:#3a6647;margin-bottom:3px;text-transform:uppercase;letter-spacing:.4px}
.hero-val{font-size:30px;font-weight:700;color:#e0f0e6;margin-bottom:4px}
.hero-change{font-size:13px}
.mini-chart{height:54px;margin-top:12px}
.mini-chart svg{width:100%;height:54px}
.tf-row{display:flex;gap:6px;margin-top:12px}
.tf{font-size:11px;padding:4px 11px;border-radius:20px;cursor:pointer;color:#3a6647;background:transparent;border:1px solid #1a3a24;transition:all .2s}
.tf.active{background:rgba(46,204,113,.15);color:#2ecc71;border-color:transparent}

/* ── SECTION HEAD ── */
.sec-head{font-size:10px;font-weight:700;color:#3a6647;padding:0 18px;margin-bottom:9px;letter-spacing:.7px;text-transform:uppercase}

/* ── AI CARD ── */
.ai-card{margin:0 16px 16px;background:#071a0e;border:1px solid #0f3a20;border-radius:14px;padding:14px 16px}
.ai-badge{display:inline-flex;align-items:center;gap:6px;background:rgba(46,204,113,.12);color:#2ecc71;font-size:10px;padding:3px 10px;border-radius:20px;margin-bottom:9px}
.ai-badge::before{content:'';width:5px;height:5px;background:#2ecc71;border-radius:50%;animation:pulse 1.8s infinite}
.ai-text{font-size:13px;color:#a0c8aa;line-height:1.6}
.ai-btns{display:flex;gap:8px;margin-top:11px}
.ai-btn{flex:1;padding:9px 4px;border-radius:10px;font-size:11px;font-weight:700;border:none;cursor:pointer;transition:opacity .2s}
.ai-btn:hover{opacity:.8}
.ab-hold{background:rgba(46,204,113,.13);color:#2ecc71}
.ab-sell{background:rgba(231,76,60,.12);color:#e74c3c}
.ab-div{background:rgba(52,152,219,.12);color:#3498db}

/* ── HOLDING ROW ── */
.h-row{display:flex;align-items:center;gap:11px;padding:12px 18px;border-bottom:1px solid #071a0e;cursor:pointer;transition:background .15s}
.h-row:hover{background:rgba(46,204,113,.04)}
.ticker{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;flex-shrink:0}
.t-gr{background:#0a2a14;color:#2ecc71}
.t-bl{background:#0a1a30;color:#3498db}
.t-am{background:#2a1a08;color:#f39c12}
.t-pi{background:#2a0a18;color:#e91e8c}
.h-info{flex:1}
.h-name{font-size:13px;font-weight:600;color:#d0e8d6}
.h-sub{font-size:11px;color:#3a6647;margin-top:2px}
.h-right{text-align:right}
.h-val{font-size:13px;font-weight:600;color:#d0e8d6}
.h-pct{font-size:11px;margin-top:2px}

/* ── ESG ── */
.esg-hero{background:#071a0e;padding:16px 20px 18px;border-bottom:1px solid #0f2a18}
.esg-big{font-size:46px;font-weight:700;color:#2ecc71}
.esg-pill{display:inline-block;background:rgba(46,204,113,.12);color:#2ecc71;font-size:11px;padding:4px 12px;border-radius:20px;margin-top:8px}
.esg-item{background:#071a0e;border-radius:12px;padding:13px 15px;margin-bottom:11px;border:1px solid #0f2a18}
.esg-bar-bg{height:6px;background:#0a2214;border-radius:3px;overflow:hidden;margin-top:8px}
.esg-bar{height:6px;border-radius:3px}

/* ── RISK MEASURER ── */
.risk-card{margin:0 16px 14px;background:#071a0e;border:1px solid #0f3a20;border-radius:14px;padding:15px 16px}
.risk-title{font-size:13px;font-weight:700;color:#d0e8d6;margin-bottom:12px}
.risk-meter{position:relative;height:16px;background:#0a2214;border-radius:8px;overflow:hidden;margin-bottom:8px}
.risk-fill{height:100%;border-radius:8px;transition:width .8s ease}
.risk-labels{display:flex;justify-content:space-between;font-size:10px;color:#3a6647}
.risk-badge{display:inline-block;font-size:11px;font-weight:700;padding:3px 12px;border-radius:20px;margin-top:8px}
.risk-sliders{margin-top:12px}
.risk-row{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.risk-row label{font-size:11px;color:#3a6647;width:90px;flex-shrink:0}
.risk-row input[type=range]{flex:1;accent-color:#2ecc71;height:4px}
.risk-row span{font-size:11px;font-weight:700;width:32px;text-align:right}

/* ── LEARN (BEGINNER) ── */
.learn-hero{background:#071a0e;padding:16px 20px;border-bottom:1px solid #0f2a18}
.learn-hero-title{font-size:16px;font-weight:700;color:#d0e8d6;margin-bottom:4px}
.learn-hero-sub{font-size:12px;color:#3a6647}
.progress-bar-bg{height:6px;background:#0a2214;border-radius:3px;overflow:hidden;margin-top:10px}
.progress-bar{height:6px;background:#2ecc71;border-radius:3px;width:30%}
.lesson-card{margin:0 16px 12px;background:#071a0e;border:1px solid #0f2a18;border-radius:14px;padding:14px 16px;cursor:pointer;transition:border-color .2s}
.lesson-card:hover{border-color:#1a5a2c}
.lesson-card.done{border-color:#0f3a20;opacity:.7}
.lc-top{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.lc-icon{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.lc-title{font-size:13px;font-weight:700;color:#d0e8d6}
.lc-sub{font-size:11px;color:#3a6647;margin-top:1px}
.lc-body{font-size:12px;color:#5a8a6a;line-height:1.6;display:none;margin-top:10px;padding-top:10px;border-top:1px solid #0f2a18}
.lc-open .lc-body{display:block}
.lc-badge{font-size:10px;padding:2px 8px;border-radius:20px;margin-left:auto;flex-shrink:0}
.tag-beg{background:rgba(46,204,113,.12);color:#2ecc71}
.tag-med{background:rgba(243,156,18,.12);color:#f39c12}
.tag-adv{background:rgba(231,76,60,.12);color:#e74c3c}

/* ── GLOSSARY ── */
.glossary-card{margin:0 16px 10px;background:#071a0e;border:1px solid #0f2a18;border-radius:12px;padding:12px 15px}
.g-term{font-size:13px;font-weight:700;color:#2ecc71;margin-bottom:4px}
.g-def{font-size:12px;color:#5a8a6a;line-height:1.5}

/* ── PROFILE ── */
.prof-hero{background:#071a0e;padding:22px;text-align:center;border-bottom:1px solid #0f2a18}
.prof-av{width:66px;height:66px;border-radius:50%;background:#0f3a1e;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:700;color:#2ecc71;margin:0 auto 12px;border:2px solid #1a5a2c}
.prof-name{font-size:17px;font-weight:700;color:#e0f0e6}
.prof-email{font-size:12px;color:#3a6647;margin-top:4px}
.prof-plan{display:inline-block;background:rgba(46,204,113,.12);color:#2ecc71;font-size:11px;padding:4px 14px;border-radius:20px;margin-top:10px}
.menu-item{display:flex;align-items:center;justify-content:space-between;padding:15px 20px;border-bottom:1px solid #071a0e;cursor:pointer;transition:background .15s}
.menu-item:hover{background:rgba(46,204,113,.04)}
.mi-left{display:flex;align-items:center;gap:12px}
.mi-icon{width:36px;height:36px;border-radius:10px;background:#0a2214;display:flex;align-items:center;justify-content:center;flex-shrink:0;border:1px solid #0f2a18}
.mi-label{font-size:14px;color:#c0d8c6}
.mi-arrow{color:#1e4a2c;font-size:16px}
.logout-btn{width:calc(100% - 36px);margin:16px 18px;background:rgba(231,76,60,.08);color:#e74c3c;border:1px solid rgba(231,76,60,.2);border-radius:12px;padding:13px;font-size:14px;font-weight:700;cursor:pointer}

/* ── NAV ── */
.nav-bar{display:flex;background:#071a0e;border-top:1px solid #0f2a18;flex-shrink:0;padding-bottom:8px}
.nav-btn{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;padding:9px 0 6px;font-size:9px;color:#3a6647;cursor:pointer;border:none;background:transparent;transition:color .2s}
.nav-btn.active{color:#2ecc71}
.nav-btn svg{width:19px;height:19px}

/* ── QUIZ ── */
.quiz-card{margin:0 16px 14px;background:#071a0e;border:1px solid #1a3a24;border-radius:14px;padding:14px 16px}
.quiz-q{font-size:13px;color:#d0e8d6;font-weight:600;margin-bottom:12px;line-height:1.5}
.quiz-opts{display:flex;flex-direction:column;gap:8px}
.quiz-opt{background:#0a2214;border:1px solid #1a3a24;border-radius:10px;padding:10px 13px;font-size:12px;color:#a0c8aa;cursor:pointer;transition:all .2s}
.quiz-opt:hover{border-color:#2ecc71;color:#2ecc71}
.quiz-opt.correct{border-color:#2ecc71;background:rgba(46,204,113,.12);color:#2ecc71}
.quiz-opt.wrong{border-color:#e74c3c;background:rgba(231,76,60,.08);color:#e74c3c}
.quiz-result{margin-top:10px;font-size:12px;line-height:1.5;display:none}
</style>
</head>
<body>
<div class="phone">

<!-- ═══════════════════════════════════════════════════
     LOGIN
══════════════════════════════════════════════════════ -->
<div id="s-login" class="screen active">
  <div class="sb"><span>9:41</span><span>●●●</span></div>
  <div class="login-body">
    <div class="brand">
      <div><div class="brand-dot"></div></div>
      <div class="brand-name">Invest<span>IQ</span></div>
      <div class="brand-tag">Smarter insights. Better decisions.</div>
    </div>
    <div class="inp-wrap">
      <div class="inp-label">Email address</div>
      <input class="inp" id="l-email" type="email" placeholder="you@email.com" value="radhika@investiq.ae">
    </div>
    <div class="inp-wrap">
      <div class="inp-label">Password</div>
      <input class="inp" id="l-pass" type="password" placeholder="••••••••" value="demo1234">
    </div>
    <div class="err" id="l-err">Wrong password — use <b>demo1234</b> for the demo.</div>
    <button class="btn-primary" onclick="doLogin()">Sign in</button>
    <div class="link-row">No account? <a onclick="show('s-signup')">Sign up free</a></div>
    <div class="link-row" style="margin-top:10px"><a>Forgot password?</a></div>
    <div class="hint">Demo: <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="95e7f4f1fdfcfef4d5fcfbe3f0e6e1fce4bbf4f0">[email&#160;protected]</a> / demo1234</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     LOADING SCREEN
══════════════════════════════════════════════════════ -->
<div id="s-loading" class="screen">
  <div class="sb"><span>9:41</span><span>●●●</span></div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;background:#071a0e;padding:40px 28px;gap:0">
    <div style="font-size:28px;font-weight:700;color:#e0f0e6;letter-spacing:.5px;margin-bottom:6px">Invest<span style="color:#2ecc71">IQ</span></div>
    <div style="font-size:13px;color:#3a6647;margin-bottom:48px">Dubai, UAE</div>
    <div style="width:56px;height:56px;border-radius:50%;border:3px solid #0f2a18;border-top-color:#2ecc71;animation:spin 0.8s linear infinite;margin-bottom:28px"></div>
    <div style="font-size:14px;font-weight:600;color:#c0d8c0;margin-bottom:10px" id="load-title">Signing you in...</div>
    <div style="font-size:12px;color:#3a6647;text-align:center;line-height:1.6" id="load-sub">Verifying credentials</div>
    <div style="width:200px;height:4px;background:#0a2214;border-radius:2px;overflow:hidden;margin-top:28px">
      <div id="load-bar" style="height:4px;background:#2ecc71;border-radius:2px;width:0%;transition:width 0.4s ease"></div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     SIGNUP
══════════════════════════════════════════════════════ -->
<div id="s-signup" class="screen">
  <div class="sb"><span>9:41</span><span>●●●</span></div>
  <div class="signup-body">
    <div class="back-link" onclick="show('s-login')">← Back</div>
    <div class="signup-title">Create account</div>
    <div class="signup-sub">Join InvestIQ — invest smarter in the UAE.</div>
    <div class="row-2">
      <div class="inp-wrap"><div class="inp-label">First name</div><input class="inp" placeholder="Radhika"></div>
      <div class="inp-wrap"><div class="inp-label">Last name</div><input class="inp" placeholder="Sharma"></div>
    </div>
    <div class="inp-wrap"><div class="inp-label">Email address</div><input class="inp" type="email" placeholder="you@email.com"></div>
    <div class="inp-wrap"><div class="inp-label">Phone</div><input class="inp" placeholder="+971 50 000 0000"></div>
    <div class="inp-wrap"><div class="inp-label">I am a...</div>
      <select class="inp" style="color:#e0f0e6">
        <option value="" style="background:#0a2214">Select investor type</option>
        <option style="background:#0a2214">Complete beginner</option>
        <option style="background:#0a2214">Intermediate investor</option>
        <option style="background:#0a2214">Experienced investor</option>
      </select>
    </div>
    <div class="inp-wrap"><div class="inp-label">Password</div><input class="inp" type="password" placeholder="Min. 8 characters"></div>
    <div class="inp-wrap"><div class="inp-label">Confirm password</div><input class="inp" type="password" placeholder="••••••••"></div>
    <div class="cb-row">
      <input type="checkbox" checked id="terms">
      <label for="terms">I agree to InvestIQ's <a>Terms of Service</a> and <a>Privacy Policy</a></label>
    </div>
    <button class="btn-primary" onclick="goApp()">Create account</button>
    <div class="link-row" style="margin-top:14px">Have an account? <a onclick="show('s-login')">Sign in</a></div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════
     MAIN APP
══════════════════════════════════════════════════════ -->
<div id="s-app" class="screen">
  <div class="sb"><span>9:41</span><span>●●●</span></div>
  <div class="app-header">
    <div class="app-logo">Invest<span>IQ</span></div>
    <div class="hdr-right">
      <div class="icon-btn">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2C5.8 2 4 3.8 4 6v3L2.5 11h11L12 9V6c0-2.2-1.8-4-4-4z" stroke="#5a8a6a" stroke-width="1.2"/><path d="M6.5 13.5c0 .8.7 1.5 1.5 1.5s1.5-.7 1.5-1.5" stroke="#5a8a6a" stroke-width="1.2"/></svg>
        <div class="badge"></div>
      </div>
      <div class="avatar" onclick="switchTab('t-prof')">RS</div>
    </div>
  </div>
  <div class="tabs">
    <div class="tab active" id="t-dash" onclick="switchTab('t-dash')">Dashboard</div>
    <div class="tab" id="t-hold" onclick="switchTab('t-hold')">Holdings</div>
    <div class="tab" id="t-risk" onclick="switchTab('t-risk')">Risk</div>
    <div class="tab" id="t-esg" onclick="switchTab('t-esg')">ESG</div>
    <div class="tab" id="t-learn" onclick="switchTab('t-learn')">Learn</div>
    <div class="tab" id="t-prof" onclick="switchTab('t-prof')">Profile</div>
  </div>

  <!-- ─── DASHBOARD ─────────────────────────────── -->
  <div class="scroll" id="tab-dash">
    <div class="hero">
      <div class="hero-greeting">Good morning, Radhika 👋</div>
      <div class="hero-label">Total portfolio value</div>
      <div class="hero-val">AED 48,320</div>
      <div class="hero-change pos">▲ +AED 1,240 (2.6%) this week</div>
      <div class="mini-chart">
        <svg viewBox="0 0 340 54" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
          <defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2ecc71" stop-opacity=".2"/><stop offset="100%" stop-color="#2ecc71" stop-opacity="0"/></linearGradient></defs>
          <path d="M0,44 L38,42 L76,46 L114,32 L152,26 L190,30 L228,18 L266,11 L304,6 L340,4" fill="none" stroke="#2ecc71" stroke-width="1.8"/>
          <path d="M0,44 L38,42 L76,46 L114,32 L152,26 L190,30 L228,18 L266,11 L304,6 L340,4 L340,54 L0,54Z" fill="url(#g1)"/>
        </svg>
      </div>
      <div class="tf-row">
        <div class="tf">1D</div><div class="tf active">1W</div><div class="tf">1M</div><div class="tf">3M</div><div class="tf">1Y</div>
      </div>
    </div>
    <div class="cards-grid">
      <div class="stat-card"><div class="sc-label">Day gain</div><div class="sc-val pos">+AED 320</div><div class="sc-sub pos">+0.67% today</div></div>
      <div class="stat-card"><div class="sc-label">Total return</div><div class="sc-val pos">+AED 6,820</div><div class="sc-sub pos">+16.4% overall</div></div>
      <div class="stat-card"><div class="sc-label">Invested</div><div class="sc-val" style="color:#d0e8d6">AED 41,500</div><div class="sc-sub neutral">4 positions</div></div>
      <div class="stat-card"><div class="sc-label">Risk level</div><div class="sc-val warn">Medium</div><div class="sc-sub neutral">Score: 58/100</div></div>
    </div>
    <div class="sec-head">AI Insight</div>
    <div class="ai-card">
      <div class="ai-badge">Smart recommendation</div>
      <div class="ai-text">Your AAPL position is up 14%. Consider taking partial profits or diversifying into a stable bond ETF to reduce concentration risk in your portfolio.</div>
      <div class="ai-btns">
        <button class="ai-btn ab-hold">Hold</button>
        <button class="ai-btn ab-sell">Sell</button>
        <button class="ai-btn ab-div">Diversify</button>
      </div>
    </div>
    <div class="sec-head">Market Movers</div>
    <div class="h-row">
      <div class="ticker t-bl">AAPL</div>
      <div class="h-info"><div class="h-name">Apple Inc.</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 824</div><div class="h-pct pos">▲ +1.4%</div></div>
    </div>
    <div class="h-row">
      <div class="ticker t-gr">MSFT</div>
      <div class="h-info"><div class="h-name">Microsoft</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 1,260</div><div class="h-pct pos">▲ +0.8%</div></div>
    </div>
    <div class="h-row">
      <div class="ticker t-am">TSLA</div>
      <div class="h-info"><div class="h-name">Tesla</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 612</div><div class="h-pct neg">▼ -2.1%</div></div>
    </div>
    <div class="h-row">
      <div class="ticker t-pi">META</div>
      <div class="h-info"><div class="h-name">Meta Platforms</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 2,180</div><div class="h-pct pos">▲ +2.7%</div></div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- ─── HOLDINGS ─────────────────────────────── -->
  <div class="scroll" id="tab-hold" style="display:none">
    <div style="padding:16px;background:#04120a">
      <div class="stat-card" style="margin-bottom:6px">
        <div class="sc-label">Total holdings value</div>
        <div class="sc-val" style="font-size:24px;color:#d0e8d6">AED 48,320</div>
        <div class="sc-sub pos">+AED 6,820 total profit (+16.4%)</div>
      </div>
    </div>
    <div class="sec-head">Your Positions</div>
    <div class="h-row">
      <div class="ticker t-bl">AAPL</div>
      <div class="h-info"><div class="h-name">Apple Inc.</div><div class="h-sub">12 shares · AED 824.50/sh</div></div>
      <div class="h-right"><div class="h-val">AED 24,100</div><div class="h-pct pos">▲ +14.2%</div></div>
    </div>
    <div class="h-row">
      <div class="ticker t-gr">MSFT</div>
      <div class="h-info"><div class="h-name">Microsoft Corp.</div><div class="h-sub">8 shares · AED 1,260/sh</div></div>
      <div class="h-right"><div class="h-val">AED 15,840</div><div class="h-pct pos">▲ +6.1%</div></div>
    </div>
    <div class="h-row">
      <div class="ticker t-am">TSLA</div>
      <div class="h-info"><div class="h-name">Tesla Inc.</div><div class="h-sub">5 shares · AED 612/sh</div></div>
      <div class="h-right"><div class="h-val">AED 8,380</div><div class="h-pct neg">▼ -3.8%</div></div>
    </div>
    <div class="h-row">
      <div class="ticker t-pi">META</div>
      <div class="h-info"><div class="h-name">Meta Platforms</div><div class="h-sub">3 shares · AED 2,180/sh</div></div>
      <div class="h-right"><div class="h-val">AED 8,000</div><div class="h-pct pos">▲ +9.3%</div></div>
    </div>
    <div style="padding:16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Portfolio Allocation</div>
      <div class="stat-card" id="alloc-wrap"></div>
    </div>
    <div style="padding:0 16px 16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Recent Activity</div>
      <div class="stat-card">
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div><div style="font-size:13px;color:#d0e8d6">Bought AAPL</div><div style="font-size:11px;color:#3a6647;margin-top:2px">Apr 2, 2026</div></div>
          <div style="text-align:right"><div style="font-size:13px;color:#d0e8d6">2 shares</div><div style="font-size:11px;color:#e74c3c">−AED 1,648</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div><div style="font-size:13px;color:#d0e8d6">Sold TSLA</div><div style="font-size:11px;color:#3a6647;margin-top:2px">Mar 28, 2026</div></div>
          <div style="text-align:right"><div style="font-size:13px;color:#d0e8d6">1 share</div><div style="font-size:11px;color:#2ecc71">+AED 636</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0">
          <div><div style="font-size:13px;color:#d0e8d6">Bought META</div><div style="font-size:11px;color:#3a6647;margin-top:2px">Mar 22, 2026</div></div>
          <div style="text-align:right"><div style="font-size:13px;color:#d0e8d6">1 share</div><div style="font-size:11px;color:#e74c3c">−AED 2,060</div></div>
        </div>
      </div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- ─── RISK MEASURER ────────────────────────── -->
  <div class="scroll" id="tab-risk" style="display:none">
    <div class="hero" style="padding-bottom:16px">
      <div style="font-size:11px;color:#3a6647;margin-bottom:3px;text-transform:uppercase;letter-spacing:.4px">Portfolio Risk Score</div>
      <div style="font-size:30px;font-weight:700;color:#f39c12" id="risk-score-big">58 / 100</div>
      <div style="font-size:12px;color:#3a6647;margin-top:4px">Based on your current holdings and market conditions</div>
    </div>

    <div style="padding:14px 16px 4px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Overall Risk Meter</div>
      <div class="risk-card" style="margin:0 0 14px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <div class="risk-title" style="margin-bottom:0">Your risk level</div>
          <div class="risk-badge" id="risk-badge" style="background:rgba(243,156,18,.13);color:#f39c12">Medium</div>
        </div>
        <div class="risk-meter">
          <div class="risk-fill" id="risk-fill" style="width:58%;background:linear-gradient(90deg,#2ecc71,#f39c12)"></div>
        </div>
        <div class="risk-labels">
          <span>Low</span><span>Medium</span><span>High</span>
        </div>
        <div style="font-size:11px;color:#5a8a6a;margin-top:10px;line-height:1.5">
          Your portfolio has moderate risk. TSLA adds volatility while MSFT provides stability. Consider rebalancing to reduce single-stock concentration.
        </div>
      </div>

      <div class="sec-head" style="padding:0;margin-bottom:10px">Risk Simulator — Adjust Your Portfolio</div>
      <div class="risk-card" style="margin:0 0 14px">
        <div style="font-size:12px;color:#5a8a6a;margin-bottom:14px;line-height:1.5">Drag the sliders to see how changes affect your risk score.</div>
        <div class="risk-sliders">
          <div class="risk-row">
            <label>AAPL weight</label>
            <input type="range" min="0" max="80" value="50" step="1" oninput="updateRisk()" id="sl-aapl">
            <span id="v-aapl" style="color:#3498db">50%</span>
          </div>
          <div class="risk-row">
            <label>MSFT weight</label>
            <input type="range" min="0" max="80" value="33" step="1" oninput="updateRisk()" id="sl-msft">
            <span id="v-msft" style="color:#2ecc71">33%</span>
          </div>
          <div class="risk-row">
            <label>TSLA weight</label>
            <input type="range" min="0" max="80" value="17" step="1" oninput="updateRisk()" id="sl-tsla">
            <span id="v-tsla" style="color:#f39c12">17%</span>
          </div>
          <div class="risk-row">
            <label>Bonds / ETFs</label>
            <input type="range" min="0" max="80" value="0" step="1" oninput="updateRisk()" id="sl-bond">
            <span id="v-bond" style="color:#5a8a6a">0%</span>
          </div>
        </div>
        <div style="margin-top:12px;border-top:1px solid #0f2a18;padding-top:12px">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <div style="font-size:12px;color:#5a8a6a">Simulated risk score</div>
            <div style="font-size:18px;font-weight:700" id="sim-score" class="warn">58</div>
          </div>
          <div class="risk-meter" style="margin-top:8px">
            <div class="risk-fill" id="sim-fill" style="width:58%;background:linear-gradient(90deg,#2ecc71,#f39c12)"></div>
          </div>
          <div style="font-size:11px;color:#3a6647;margin-top:6px" id="sim-tip">Add bonds or reduce TSLA to lower your risk.</div>
        </div>
      </div>

      <div class="sec-head" style="padding:0;margin-bottom:10px">Risk By Holding</div>
      <div class="stat-card" style="margin-bottom:14px">
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-bl" style="width:32px;height:32px;font-size:9px">AAPL</div><div><div style="font-size:13px;color:#d0e8d6">Apple</div><div style="font-size:10px;color:#3a6647">Beta: 1.2 — Moderate</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#f39c12">Medium</div><div style="font-size:10px;color:#3a6647">50% of portfolio</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-gr" style="width:32px;height:32px;font-size:9px">MSFT</div><div><div style="font-size:13px;color:#d0e8d6">Microsoft</div><div style="font-size:10px;color:#3a6647">Beta: 0.9 — Low</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#2ecc71">Low</div><div style="font-size:10px;color:#3a6647">33% of portfolio</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-am" style="width:32px;height:32px;font-size:9px">TSLA</div><div><div style="font-size:13px;color:#d0e8d6">Tesla</div><div style="font-size:10px;color:#3a6647">Beta: 2.1 — High</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#e74c3c">High</div><div style="font-size:10px;color:#3a6647">17% of portfolio</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-pi" style="width:32px;height:32px;font-size:9px">META</div><div><div style="font-size:13px;color:#d0e8d6">Meta</div><div style="font-size:10px;color:#3a6647">Beta: 1.5 — Moderate</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#f39c12">Medium</div><div style="font-size:10px;color:#3a6647">17% of portfolio</div></div>
        </div>
      </div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- ─── ESG ───────────────────────────────────── -->
  <div class="scroll" id="tab-esg" style="display:none">
    <div class="esg-hero">
      <div style="font-size:11px;color:#3a6647;margin-bottom:4px;text-transform:uppercase;letter-spacing:.4px">Portfolio ESG Score</div>
      <div class="esg-big">72</div>
      <div style="font-size:12px;color:#3a6647;margin-top:4px">Based on your 4 active holdings · Updated daily</div>
      <div class="esg-pill">Above UAE market average (64)</div>
    </div>
    <div style="padding:16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Score Breakdown</div>
      <div class="esg-item">
        <div style="display:flex;justify-content:space-between"><span style="font-size:13px;font-weight:700;color:#d0e8d6">Environmental</span><span style="font-size:13px;font-weight:700;color:#2ecc71">72</span></div>
        <div class="esg-bar-bg"><div class="esg-bar" style="width:72%;background:#2ecc71"></div></div>
        <div style="font-size:11px;color:#3a6647;margin-top:6px">Low carbon footprint. MSFT leads with carbon-neutral operations.</div>
      </div>
      <div class="esg-item">
        <div style="display:flex;justify-content:space-between"><span style="font-size:13px;font-weight:700;color:#d0e8d6">Social</span><span style="font-size:13px;font-weight:700;color:#3498db">65</span></div>
        <div class="esg-bar-bg"><div class="esg-bar" style="width:65%;background:#3498db"></div></div>
        <div style="font-size:11px;color:#3a6647;margin-top:6px">Fair labour practices. META scores lower on platform safety.</div>
      </div>
      <div class="esg-item">
        <div style="display:flex;justify-content:space-between"><span style="font-size:13px;font-weight:700;color:#d0e8d6">Governance</span><span style="font-size:13px;font-weight:700;color:#f39c12">80</span></div>
        <div class="esg-bar-bg"><div class="esg-bar" style="width:80%;background:#f39c12"></div></div>
        <div style="font-size:11px;color:#3a6647;margin-top:6px">Strong board structure and financial transparency.</div>
      </div>
      <div class="sec-head" style="padding:0;margin:14px 0 10px">Holdings ESG Rating</div>
      <div class="stat-card">
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18;font-size:11px;color:#3a6647"><span>Company</span><span>ESG Rating</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #0f2a18"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-gr" style="width:30px;height:30px;font-size:9px">MSFT</div><span style="font-size:13px;color:#d0e8d6">Microsoft</span></div><span style="color:#2ecc71;font-weight:700;font-size:13px">85 / AA</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #0f2a18"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-bl" style="width:30px;height:30px;font-size:9px">AAPL</div><span style="font-size:13px;color:#d0e8d6">Apple</span></div><span style="color:#2ecc71;font-weight:700;font-size:13px">78 / A</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #0f2a18"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-am" style="width:30px;height:30px;font-size:9px">TSLA</div><span style="font-size:13px;color:#d0e8d6">Tesla</span></div><span style="color:#f39c12;font-weight:700;font-size:13px">54 / B</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-pi" style="width:30px;height:30px;font-size:9px">META</div><span style="font-size:13px;color:#d0e8d6">Meta</span></div><span style="color:#e74c3c;font-weight:700;font-size:13px">48 / C</span></div>
      </div>
      <div class="ai-card" style="margin:12px 0 0">
        <div class="ai-badge">ESG Tip</div>
        <div class="ai-text">Replacing META with a higher-rated ESG alternative (e.g. clean energy ETF) could lift your Social score from 65 to ~73.</div>
      </div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- ─── LEARN ──────────────────────────────────── -->
  <div class="scroll" id="tab-learn" style="display:none">
    <div class="learn-hero">
      <div class="learn-hero-title">Learn</div>
      <div class="learn-hero-sub">Test your knowledge and look up key terms.</div>
    </div>

    <div style="padding:16px 0 4px">
      <div class="sec-head">Quick Quiz</div>
      <div class="quiz-card">
        <div style="font-size:10px;color:#3a6647;margin-bottom:8px;letter-spacing:.3px" id="q-counter">Question 1 of 4</div>
        <div class="quiz-q" id="q-text">What does "diversification" mean in investing?</div>
        <div class="quiz-opts" id="q-opts">
          <div class="quiz-opt" onclick="answerQ(this, false)">Putting all your money in one company</div>
          <div class="quiz-opt" onclick="answerQ(this, true)">Spreading money across different investments to reduce risk</div>
          <div class="quiz-opt" onclick="answerQ(this, false)">Only investing in bonds</div>
          <div class="quiz-opt" onclick="answerQ(this, false)">Selling stocks when prices drop</div>
        </div>
        <div class="quiz-result pos" id="q-result" style="font-size:12px;margin-top:10px;display:none"></div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px">
          <div style="font-size:11px;color:#3a6647" id="q-score">Score: 0 / 0</div>
          <button style="background:rgba(46,204,113,.12);color:#2ecc71;border:none;border-radius:8px;padding:7px 14px;font-size:11px;font-weight:700;cursor:pointer" onclick="nextQ()">Next →</button>
        </div>
      </div>

      <div class="sec-head" style="margin-top:8px">Key Terms Glossary</div>
      <div class="glossary-card">
        <div class="g-term">Bull Market</div>
        <div class="g-def">A period when stock prices are rising (20%+ from lows). Investors are optimistic and confident.</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">Bear Market</div>
        <div class="g-def">A period of falling prices (20%+ drop from highs). Can be a buying opportunity for long-term investors.</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">Dividend</div>
        <div class="g-def">Cash payments companies send to shareholders, usually quarterly — a sign the company is profitable.</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">Market Capitalisation</div>
        <div class="g-def">Total value of a company's shares. Share price × total shares = market cap. Apple is ~$3 trillion.</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">ETF (Exchange-Traded Fund)</div>
        <div class="g-def">A basket of stocks you buy as one investment — instant diversification. The S&amp;P 500 ETF holds 500 companies.</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">Beta</div>
        <div class="g-def">Measures a stock's volatility vs the market. Beta &gt; 1 = more volatile (e.g. Tesla 2.1). Beta &lt; 1 = more stable (e.g. MSFT 0.9).</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">P/E Ratio</div>
        <div class="g-def">Price ÷ Earnings Per Share. Shows how much you pay for every AED 1 of profit. High P/E = high growth expectations.</div>
      </div>
      <div class="glossary-card">
        <div class="g-term">Diversification</div>
        <div class="g-def">Spreading investments across different assets so one bad pick doesn't sink your whole portfolio.</div>
      </div>
    </div>
    <div style="height:24px"></div>
  </div>

  <!-- ─── PROFILE ────────────────────────────────── -->
  <div class="scroll" id="tab-prof" style="display:none">
    <div class="prof-hero">
      <div class="prof-av">RS</div>
      <div class="prof-name">Radhika Sharma</div>
      <div class="prof-email"><a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b6c4d7d2dedfddd7f6dfd8c0d3c5c2dfc798d7d3">[email&#160;protected]</a></div>
      <div class="prof-plan">Pro Plan · AED 49/mo</div>
    </div>
    <div style="padding-top:6px">
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="5" r="3" stroke="#2ecc71" stroke-width="1.2"/><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Account details</span></div>
        <span class="mi-arrow">›</span>
      </div>
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="3" width="12" height="10" rx="2" stroke="#2ecc71" stroke-width="1.2"/><path d="M5 7h6M5 10h4" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Subscription & billing</span></div>
        <span class="mi-arrow">›</span>
      </div>
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2l1 3h3l-2.5 1.8 1 3L8 8.2 5.5 9.8l1-3L4 5h3z" stroke="#2ecc71" stroke-width="1.2" stroke-linejoin="round"/></svg></div><span class="mi-label">ESG preferences</span></div>
        <span class="mi-arrow">›</span>
      </div>
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2ecc71" stroke-width="1.2"/><path d="M8 5v4M8 11v.5" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Risk profile settings</span></div>
        <span class="mi-arrow">›</span>
      </div>
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2C5.8 2 4 3.8 4 6v3L2.5 11h11L12 9V6c0-2.2-1.8-4-4-4z" stroke="#2ecc71" stroke-width="1.2"/><path d="M6.5 13.5c0 .8.7 1.5 1.5 1.5s1.5-.7 1.5-1.5" stroke="#2ecc71" stroke-width="1.2"/></svg></div><span class="mi-label">Notifications</span></div>
        <span class="mi-arrow">›</span>
      </div>
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="2" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/><rect x="9" y="2" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/><rect x="2" y="9" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/><rect x="9" y="9" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/></svg></div><span class="mi-label">Investor Academy progress</span></div>
        <span class="mi-arrow">›</span>
      </div>
      <div class="menu-item">
        <div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 4h12M2 8h8M2 12h10" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Help & support</span></div>
        <span class="mi-arrow">›</span>
      </div>
    </div>
    <button class="logout-btn" onclick="show('s-login')">Sign out of InvestIQ</button>
    <div style="text-align:center;font-size:11px;color:#1a3a24;padding-bottom:20px">InvestIQ v2.0 · Dubai, UAE · Not regulated financial advice — prototype only.</div>
  </div>

  <!-- ─── BOTTOM NAV ─────────────────────────────── -->
  <div class="nav-bar">
    <button class="nav-btn active" id="nb-dash" onclick="switchTab('t-dash')">
      <svg viewBox="0 0 20 20" fill="none"><rect x="1" y="10" width="5" height="8" rx="1" fill="currentColor"/><rect x="7.5" y="6" width="5" height="12" rx="1" fill="currentColor"/><rect x="14" y="2" width="5" height="16" rx="1" fill="currentColor"/></svg>
      Home
    </button>
    <button class="nav-btn" id="nb-hold" onclick="switchTab('t-hold')">
      <svg viewBox="0 0 20 20" fill="none"><rect x="2" y="2" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M6 10h8M6 13.5h5M6 6.5h8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      Holdings
    </button>
    <button class="nav-btn" id="nb-risk" onclick="switchTab('t-risk')">
      <svg viewBox="0 0 20 20" fill="none"><path d="M10 2L2 17h16L10 2z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M10 8v4M10 14v.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      Risk
    </button>
    <button class="nav-btn" id="nb-esg" onclick="switchTab('t-esg')">
      <svg viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="7.5" stroke="currentColor" stroke-width="1.4"/><path d="M7 10l2 2 4-4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      ESG
    </button>
    <button class="nav-btn" id="nb-learn" onclick="switchTab('t-learn')">
      <svg viewBox="0 0 20 20" fill="none"><path d="M10 3L2 7l8 4 8-4-8-4z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M2 7v6M18 7v6M6 9v5a4 4 0 008 0V9" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      Learn
    </button>
    <button class="nav-btn" id="nb-prof" onclick="switchTab('t-prof')">
      <svg viewBox="0 0 20 20" fill="none"><circle cx="10" cy="7" r="3.5" stroke="currentColor" stroke-width="1.4"/><path d="M3 18c0-3.9 3.1-7 7-7s7 3.1 7 7" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      Profile
    </button>
  </div>
</div>

</div>

<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>
// ── NAVIGATION ──────────────────────────────────────
function show(id){
  document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}
function doLogin(){
  var p=document.getElementById('l-pass').value;
  var e=document.getElementById('l-err');
  if(p==='demo1234'){
    e.style.display='none';
    runLoadingSequence(function(){show('s-app');switchTab('t-dash');});
  } else {
    e.style.display='block';
  }
}
function goApp(){
  runLoadingSequence(function(){show('s-app');switchTab('t-dash');});
}
function runLoadingSequence(callback){
  show('s-loading');
  var bar=document.getElementById('load-bar');
  var title=document.getElementById('load-title');
  var sub=document.getElementById('load-sub');
  var steps=[
    {w:'15%', t:'Signing you in...', s:'Verifying credentials'},
    {w:'35%', t:'Signing you in...', s:'Authentication successful'},
    {w:'55%', t:'Loading your portfolio...', s:'Fetching holdings & prices'},
    {w:'72%', t:'Calculating insights...', s:'Running AI risk analysis'},
    {w:'88%', t:'Calculating insights...', s:'Preparing ESG scores'},
    {w:'100%',t:'Almost there...', s:'Building your dashboard'},
  ];
  var i=0;
  function tick(){
    if(i>=steps.length){setTimeout(callback,300);return;}
    var s=steps[i];
    bar.style.width=s.w;
    title.textContent=s.t;
    sub.textContent=s.s;
    i++;
    setTimeout(tick, i===1?400:320);
  }
  tick();
}

var TABS={
  't-dash':['nb-dash','tab-dash'],
  't-hold':['nb-hold','tab-hold'],
  't-risk':['nb-risk','tab-risk'],
  't-esg':['nb-esg','tab-esg'],
  't-learn':['nb-learn','tab-learn'],
  't-prof':['nb-prof','tab-prof']
};
function switchTab(id){
  document.querySelectorAll('.tab,.nav-btn').forEach(el=>el.classList.remove('active'));
  Object.values(TABS).forEach(function(v){
    var c=document.getElementById(v[1]);
    if(c)c.style.display='none';
  });
  document.getElementById(id).classList.add('active');
  var t=TABS[id];
  if(t){
    var nb=document.getElementById(t[0]);
    if(nb)nb.classList.add('active');
    var tc=document.getElementById(t[1]);
    if(tc)tc.style.display='block';
  }
}

// ── ALLOCATION BARS ─────────────────────────────────
var allocs=[{n:'AAPL',p:50,c:'#3498db'},{n:'MSFT',p:33,c:'#2ecc71'},{n:'TSLA',p:17,c:'#f39c12'},{n:'META',p:17,c:'#e91e8c'}];
var total=allocs.reduce(function(a,b){return a+b.p;},0);
var aw=document.getElementById('alloc-wrap');
if(aw){allocs.forEach(function(a){
  var pct=Math.round(a.p/total*100);
  aw.innerHTML+='<div style="margin-bottom:12px"><div style="display:flex;justify-content:space-between;font-size:12px;color:#5a8a6a;margin-bottom:4px"><span>'+a.n+'</span><span>'+pct+'%</span></div><div style="height:5px;background:#0a2214;border-radius:3px;overflow:hidden"><div style="width:'+pct+'%;height:5px;background:'+a.c+';border-radius:3px"></div></div></div>';
});}

// ── TIME FILTER ─────────────────────────────────────
document.querySelectorAll('.tf').forEach(function(b){
  b.addEventListener('click',function(){
    document.querySelectorAll('.tf').forEach(function(x){x.classList.remove('active');});
    this.classList.add('active');
  });
});

// ── RISK SIMULATOR ──────────────────────────────────
var RISK={aapl:1.2,msft:0.9,tsla:2.1,bond:0.2};
function updateRisk(){
  var w={
    aapl:parseInt(document.getElementById('sl-aapl').value),
    msft:parseInt(document.getElementById('sl-msft').value),
    tsla:parseInt(document.getElementById('sl-tsla').value),
    bond:parseInt(document.getElementById('sl-bond').value)
  };
  document.getElementById('v-aapl').textContent=w.aapl+'%';
  document.getElementById('v-msft').textContent=w.msft+'%';
  document.getElementById('v-tsla').textContent=w.tsla+'%';
  document.getElementById('v-bond').textContent=w.bond+'%';
  var total=w.aapl+w.msft+w.tsla+w.bond||1;
  var score=(w.aapl/total*RISK.aapl + w.msft/total*RISK.msft + w.tsla/total*RISK.tsla + w.bond/total*RISK.bond);
  var pct=Math.min(Math.round(score/2.1*100),100);
  var el=document.getElementById('sim-score');
  var fill=document.getElementById('sim-fill');
  var tip=document.getElementById('sim-tip');
  el.textContent=pct;
  fill.style.width=pct+'%';
  if(pct<35){
    el.className='pos';fill.style.background='#2ecc71';
    tip.textContent='Low risk portfolio — great for capital preservation.';
  } else if(pct<65){
    el.className='warn';fill.style.background='linear-gradient(90deg,#2ecc71,#f39c12)';
    tip.textContent='Balanced risk. A good mix for moderate growth.';
  } else {
    el.className='neg';fill.style.background='linear-gradient(90deg,#f39c12,#e74c3c)';
    tip.textContent='High risk! Consider adding bonds or stable stocks.';
  }
}

// ── LESSON TOGGLE ────────────────────────────────────
function toggleLesson(el){
  el.classList.toggle('lc-open');
}

// ── QUIZ ─────────────────────────────────────────────
var QS=[
  {q:"What does 'diversification' mean in investing?",opts:["Putting all your money in one company","Spreading money across different investments to reduce risk","Only investing in bonds","Selling stocks when prices drop"],a:1},
  {q:"What does a high P/E ratio suggest about a stock?",opts:["The company is losing money","Investors have high growth expectations","The stock is cheap","The company pays large dividends"],a:1},
  {q:"What is 'Beta' in stock analysis?",opts:["The stock's dividend yield","A measure of a stock's volatility vs the market","The company's profit margin","The annual return of a stock"],a:1},
  {q:"What does ESG stand for?",opts:["Earnings, Sales, Growth","Environmental, Social, Governance","Equity, Stocks, Gold","Earnings, Shares, Gains"],a:1},
  {q:"What is a Bull Market?",opts:["Prices falling 20%+ from highs","A market with no volatility","Prices rising 20%+ from lows","A market only for bonds"],a:2},
  {q:"What does an ETF give you?",opts:["Ownership of one company","A fixed interest payment","Exposure to a basket of stocks","A guaranteed return"],a:2},
];
var qi=0,correct_count=0,answered=0;
function loadQ(){
  var q=QS[qi%QS.length];
  var counter=document.getElementById('q-counter');
  if(counter)counter.textContent='Question '+(qi%QS.length+1)+' of '+QS.length;
  document.getElementById('q-text').textContent=q.q;
  var opts=document.getElementById('q-opts');
  opts.innerHTML='';
  var res=document.getElementById('q-result');
  if(res){res.style.display='none';res.textContent='';}
  q.opts.forEach(function(o,i){
    var d=document.createElement('div');
    d.className='quiz-opt';
    d.textContent=o;
    d.onclick=function(){answerQ(d,i===q.a);};
    opts.appendChild(d);
  });
}
function answerQ(el,correct){
  document.querySelectorAll('.quiz-opt').forEach(function(o){o.onclick=null;o.style.opacity='.5';});
  el.style.opacity='1';
  el.classList.add(correct?'correct':'wrong');
  answered++;
  if(correct)correct_count++;
  var res=document.getElementById('q-result');
  if(res){
    res.style.display='block';
    if(correct){res.textContent='Correct!';res.style.color='#2ecc71';}
    else{
      res.textContent='Not quite — correct answer shown.';res.style.color='#e74c3c';
      var correctOpt=document.querySelectorAll('.quiz-opt')[QS[qi%QS.length].a];
      correctOpt.classList.add('correct');correctOpt.style.opacity='1';
    }
  }
  var sc=document.getElementById('q-score');
  if(sc)sc.textContent='Score: '+correct_count+' / '+answered;
}
function nextQ(){qi++;loadQ();}
loadQ();
</script>
</body>
</html>"""

components.html(HTML, height=860, scrolling=False)
