<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>InvestIQ</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#04120a;display:flex;justify-content:center;padding:10px;min-height:100vh}
.phone{width:390px;border-radius:42px;border:2px solid #1a3a24;background:#071a0e;overflow:hidden;display:flex;flex-direction:column;min-height:800px}
.screen{display:none;flex-direction:column;flex:1}
.screen.active{display:flex}
.sb{background:#071a0e;display:flex;justify-content:space-between;padding:12px 24px 6px;font-size:11px;color:#3a6647;flex-shrink:0}
.inp{width:100%;background:#0a2214;border:1.5px solid #1a3a24;border-radius:12px;padding:13px 16px;font-size:14px;color:#e0f0e6;outline:none;transition:border-color .2s}
.inp:focus{border-color:#2ecc71}
.inp::placeholder{color:#1e4a2c}
.inp-wrap{margin-bottom:16px}
.inp-label{font-size:12px;color:#5a8a6a;margin-bottom:6px}
.btn-primary{width:100%;background:#2ecc71;color:#03100a;border:none;border-radius:12px;padding:14px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;letter-spacing:.3px}
.btn-primary:hover{background:#27ae60}
.btn-primary:active{transform:scale(.98)}
.link-row{text-align:center;margin-top:18px;font-size:13px;color:#3a6647}
.link-row a{color:#2ecc71;cursor:pointer;text-decoration:none}
.err{font-size:12px;color:#e74c3c;margin-top:-10px;margin-bottom:12px;display:none}
.hint{text-align:center;font-size:11px;color:#1e4a2c;margin-top:20px}
.login-body{flex:1;display:flex;flex-direction:column;justify-content:center;padding:36px 28px;background:#071a0e}
.brand{text-align:center;margin-bottom:40px}
.brand-name{font-size:34px;font-weight:700;color:#e0f0e6;letter-spacing:.5px}
.brand-name span{color:#2ecc71}
.brand-tag{font-size:13px;color:#3a6647;margin-top:8px}
.brand-dot{width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;margin-bottom:16px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.6;transform:scale(.8)}}
@keyframes spin{to{transform:rotate(360deg)}}
.signup-body{flex:1;display:flex;flex-direction:column;padding:26px 28px;background:#071a0e;overflow-y:auto}
.back-link{color:#2ecc71;font-size:13px;cursor:pointer;margin-bottom:18px}
.signup-title{font-size:22px;font-weight:700;color:#e0f0e6;margin-bottom:6px}
.signup-sub{font-size:13px;color:#3a6647;margin-bottom:22px}
.row-2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cb-row{display:flex;gap:10px;align-items:flex-start;margin-bottom:20px}
.cb-row label{font-size:12px;color:#3a6647;line-height:1.6}
.cb-row a{color:#2ecc71}
.app-header{background:#071a0e;padding:13px 20px 11px;display:flex;justify-content:space-between;align-items:center;flex-shrink:0;border-bottom:1px solid #0f2a18}
.app-logo{font-size:17px;font-weight:700;color:#e0f0e6}
.app-logo span{color:#2ecc71}
.hdr-right{display:flex;gap:10px;align-items:center}
.icon-btn{width:34px;height:34px;border-radius:50%;background:#0a2214;display:flex;align-items:center;justify-content:center;cursor:pointer;border:1px solid #1a3a24;position:relative}
.badge{width:8px;height:8px;background:#2ecc71;border-radius:50%;position:absolute;top:5px;right:5px;border:1.5px solid #071a0e}
.avatar{width:34px;height:34px;border-radius:50%;background:#0f3a1e;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#2ecc71;cursor:pointer;border:1px solid #1a5a2c}
.tabs{display:flex;background:#071a0e;border-bottom:1px solid #0f2a18;flex-shrink:0;overflow-x:auto}
.tabs::-webkit-scrollbar{height:0}
.tab{flex:1;min-width:60px;padding:11px 4px;font-size:10px;color:#3a6647;text-align:center;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .2s}
.tab.active{color:#2ecc71;border-bottom-color:#2ecc71}
.scroll{flex:1;overflow-y:auto;background:#04120a}
.scroll::-webkit-scrollbar{width:0}
.pos{color:#2ecc71}
.neg{color:#e74c3c}
.neutral{color:#3a6647}
.warn{color:#f39c12}
.stat-card{background:#071a0e;border-radius:12px;padding:13px 15px;border:1px solid #0f2a18}
.sc-label{font-size:10px;color:#3a6647;margin-bottom:5px;text-transform:uppercase;letter-spacing:.4px}
.sc-val{font-size:19px;font-weight:700;color:#e0f0e6}
.sc-sub{font-size:11px;margin-top:3px}
.cards-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:16px}
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
.sec-head{font-size:10px;font-weight:700;color:#3a6647;padding:0 18px;margin-bottom:9px;letter-spacing:.7px;text-transform:uppercase}
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
.h-row{display:flex;align-items:center;gap:11px;padding:12px 18px;border-bottom:1px solid #071a0e;cursor:pointer;transition:background .15s}
.h-row:hover{background:rgba(46,204,113,.04)}
.ticker{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;flex-shrink:0}
.t-gr{background:#0a2a14;color:#2ecc71}
.t-bl{background:#0a1a30;color:#3498db}
.t-am{background:#2a1a08;color:#f39c12}
.t-pi{background:#2a0a18;color:#e91e8c}
.t-pu{background:#1a0a2a;color:#9b59b6}
.h-info{flex:1}
.h-name{font-size:13px;font-weight:600;color:#d0e8d6}
.h-sub{font-size:11px;color:#3a6647;margin-top:2px}
.h-right{text-align:right}
.h-val{font-size:13px;font-weight:600;color:#d0e8d6}
.h-pct{font-size:11px;margin-top:2px}
.esg-hero{background:#071a0e;padding:16px 20px 18px;border-bottom:1px solid #0f2a18}
.esg-big{font-size:46px;font-weight:700;color:#2ecc71}
.esg-pill{display:inline-block;background:rgba(46,204,113,.12);color:#2ecc71;font-size:11px;padding:4px 12px;border-radius:20px;margin-top:8px}
.esg-item{background:#071a0e;border-radius:12px;padding:13px 15px;margin-bottom:11px;border:1px solid #0f2a18}
.esg-bar-bg{height:6px;background:#0a2214;border-radius:3px;overflow:hidden;margin-top:8px}
.esg-bar{height:6px;border-radius:3px}
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
.learn-hero{background:#071a0e;padding:16px 20px;border-bottom:1px solid #0f2a18}
.learn-hero-title{font-size:16px;font-weight:700;color:#d0e8d6;margin-bottom:4px}
.learn-hero-sub{font-size:12px;color:#3a6647}
.progress-bar-bg{height:6px;background:#0a2214;border-radius:3px;overflow:hidden;margin-top:10px}
.progress-bar{height:6px;background:#2ecc71;border-radius:3px;width:30%}
.glossary-card{margin:0 16px 10px;background:#071a0e;border:1px solid #0f2a18;border-radius:12px;padding:12px 15px}
.g-term{font-size:13px;font-weight:700;color:#2ecc71;margin-bottom:4px}
.g-def{font-size:12px;color:#5a8a6a;line-height:1.5}
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
.nav-bar{display:flex;background:#071a0e;border-top:1px solid #0f2a18;flex-shrink:0;padding-bottom:8px}
.nav-btn{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;padding:9px 0 6px;font-size:9px;color:#3a6647;cursor:pointer;border:none;background:transparent;transition:color .2s}
.nav-btn.active{color:#2ecc71}
.nav-btn svg{width:19px;height:19px}
.trade-seg{display:flex;background:#0a2214;border-radius:10px;padding:3px;margin:0 16px 14px}
.trade-seg-btn{flex:1;padding:8px 0;font-size:12px;font-weight:700;border:none;background:transparent;color:#3a6647;border-radius:8px;cursor:pointer;transition:all .2s}
.trade-seg-btn.active{background:#2ecc71;color:#03100a}
.stock-pick{margin:0 16px 12px}
.stock-pick-label{font-size:11px;color:#3a6647;margin-bottom:6px;text-transform:uppercase;letter-spacing:.4px}
.stock-btn-row{display:flex;gap:8px;flex-wrap:wrap}
.stock-btn{padding:7px 14px;border-radius:20px;border:1px solid #1a3a24;background:#071a0e;font-size:12px;font-weight:700;color:#5a8a6a;cursor:pointer;transition:all .2s}
.stock-btn.active{background:#0a2a14;border-color:#2ecc71;color:#2ecc71}
.trade-form{margin:0 16px 14px;background:#071a0e;border:1px solid #0f2a18;border-radius:14px;padding:14px 16px}
.trade-stock-header{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.trade-price-row{display:flex;justify-content:space-between;margin-bottom:12px}
.trade-price-label{font-size:11px;color:#3a6647}
.trade-price-val{font-size:13px;font-weight:700;color:#d0e8d6}
.qty-row{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.qty-row label{font-size:11px;color:#3a6647;width:70px;flex-shrink:0}
.qty-btn{width:30px;height:30px;border-radius:50%;border:1px solid #1a3a24;background:#0a2214;color:#2ecc71;font-size:18px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;line-height:1}
.qty-input{flex:1;background:#0a2214;border:1px solid #1a3a24;border-radius:8px;padding:6px 10px;font-size:14px;color:#e0f0e6;text-align:center;outline:none;width:60px}
.trade-summary{background:#0a2214;border-radius:10px;padding:10px 12px;margin-bottom:14px}
.trade-summary-row{display:flex;justify-content:space-between;font-size:12px;margin-bottom:5px}
.trade-summary-row:last-child{margin-bottom:0;border-top:1px solid #1a3a24;padding-top:5px;font-weight:700}
.btn-buy{width:100%;background:#2ecc71;color:#03100a;border:none;border-radius:11px;padding:13px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s}
.btn-buy:active{opacity:.85;transform:scale(.98)}
.btn-sell-red{width:100%;background:#e74c3c;color:#fff;border:none;border-radius:11px;padding:13px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s}
.btn-sell-red:active{opacity:.85;transform:scale(.98)}
.rebal-card{margin:0 16px 12px;background:#071a0e;border:1px solid #0f2a18;border-radius:14px;padding:14px 16px}
.rebal-row{display:flex;align-items:center;gap:8px;margin-bottom:11px}
.rebal-ticker{width:38px;height:38px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700;flex-shrink:0}
.rebal-bars{flex:1}
.rebal-label{display:flex;justify-content:space-between;font-size:10px;color:#3a6647;margin-bottom:3px}
.rebal-track{height:6px;background:#0a2214;border-radius:3px;overflow:hidden;position:relative}
.rebal-current{height:6px;border-radius:3px;transition:width .6s ease}
.rebal-target-line{position:absolute;top:0;width:2px;height:6px;background:#fff;opacity:.5;border-radius:1px}
.rebal-action{font-size:10px;font-weight:700;text-align:right;white-space:nowrap;flex-shrink:0;min-width:72px}
.quiz-card{margin:0 16px 14px;background:#071a0e;border:1px solid #1a3a24;border-radius:14px;padding:14px 16px}
.quiz-q{font-size:13px;color:#d0e8d6;font-weight:600;margin-bottom:12px;line-height:1.5}
.quiz-opts{display:flex;flex-direction:column;gap:8px}
.quiz-opt{background:#0a2214;border:1px solid #1a3a24;border-radius:10px;padding:10px 13px;font-size:12px;color:#a0c8aa;cursor:pointer;transition:all .2s}
.quiz-opt:hover{border-color:#2ecc71;color:#2ecc71}
.quiz-opt.correct{border-color:#2ecc71;background:rgba(46,204,113,.12);color:#2ecc71}
.quiz-opt.wrong{border-color:#e74c3c;background:rgba(231,76,60,.08);color:#e74c3c}
.trade-toast{position:absolute;bottom:80px;left:50%;transform:translateX(-50%);background:#0f3a1e;border:1px solid #2ecc71;border-radius:10px;padding:10px 20px;font-size:12px;color:#2ecc71;font-weight:700;display:none;z-index:999;white-space:nowrap}
.trade-toast.sell-toast{background:#3a0e0e;border-color:#e74c3c;color:#e74c3c}
.upload-zone{border:2px dashed #1a3a24;border-radius:12px;padding:20px;text-align:center;cursor:pointer;transition:border-color .2s;margin-bottom:14px}
.upload-zone:hover{border-color:#2ecc71}
.upload-zone.active{border-color:#2ecc71;background:rgba(46,204,113,.05)}
.upload-btn{background:rgba(46,204,113,.12);color:#2ecc71;border:1px solid #2ecc71;border-radius:8px;padding:8px 16px;font-size:12px;font-weight:700;cursor:pointer;margin-top:8px}
</style>
</head>
<body>
<div class="phone" style="position:relative">

<!-- LOGIN -->
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
    <div class="hint">Demo: radhika@investiq.ae / demo1234</div>
  </div>
</div>

<!-- LOADING -->
<div id="s-loading" class="screen">
  <div class="sb"><span>9:41</span><span>●●●</span></div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;background:#071a0e;padding:40px 28px">
    <div style="font-size:28px;font-weight:700;color:#e0f0e6;margin-bottom:6px">Invest<span style="color:#2ecc71">IQ</span></div>
    <div style="font-size:13px;color:#3a6647;margin-bottom:48px">Dubai, UAE</div>
    <div style="width:56px;height:56px;border-radius:50%;border:3px solid #0f2a18;border-top-color:#2ecc71;animation:spin 0.8s linear infinite;margin-bottom:28px"></div>
    <div style="font-size:14px;font-weight:600;color:#c0d8c0;margin-bottom:10px" id="load-title">Signing you in...</div>
    <div style="font-size:12px;color:#3a6647;text-align:center" id="load-sub">Verifying credentials</div>
    <div style="width:200px;height:4px;background:#0a2214;border-radius:2px;overflow:hidden;margin-top:28px">
      <div id="load-bar" style="height:4px;background:#2ecc71;border-radius:2px;width:0%;transition:width 0.4s ease"></div>
    </div>
  </div>
</div>

<!-- SIGNUP -->
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
    <div class="inp-wrap"><div class="inp-label">Email</div><input class="inp" type="email" placeholder="you@email.com"></div>
    <div class="inp-wrap"><div class="inp-label">Phone</div><input class="inp" placeholder="+971 50 000 0000"></div>
    <div class="inp-wrap"><div class="inp-label">Investor type</div>
      <select class="inp" style="color:#e0f0e6">
        <option value="" style="background:#0a2214">Select investor type</option>
        <option style="background:#0a2214">Complete beginner</option>
        <option style="background:#0a2214">Intermediate investor</option>
        <option style="background:#0a2214">Experienced investor</option>
      </select>
    </div>
    <div class="inp-wrap"><div class="inp-label">Password</div><input class="inp" type="password" placeholder="Min. 8 characters"></div>
    <div class="inp-wrap"><div class="inp-label">Confirm password</div><input class="inp" type="password" placeholder="••••••••"></div>
    <div class="cb-row"><input type="checkbox" checked id="terms"><label for="terms">I agree to InvestIQ's <a>Terms of Service</a> and <a>Privacy Policy</a></label></div>
    <button class="btn-primary" onclick="goApp()">Create account</button>
    <div class="link-row" style="margin-top:14px">Have an account? <a onclick="show('s-login')">Sign in</a></div>
  </div>
</div>

<!-- MAIN APP -->
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
    <div class="tab active" id="t-dash" onclick="switchTab('t-dash')">Home</div>
    <div class="tab" id="t-hold" onclick="switchTab('t-hold')">Holdings</div>
    <div class="tab" id="t-trade" onclick="switchTab('t-trade')">Trade</div>
    <div class="tab" id="t-rebal" onclick="switchTab('t-rebal')">Rebalance</div>
    <div class="tab" id="t-risk" onclick="switchTab('t-risk')">Risk</div>
    <div class="tab" id="t-esg" onclick="switchTab('t-esg')">ESG</div>
    <div class="tab" id="t-learn" onclick="switchTab('t-learn')">Learn</div>
    <div class="tab" id="t-prof" onclick="switchTab('t-prof')">Profile</div>
  </div>

  <!-- DASHBOARD -->
  <div class="scroll" id="tab-dash">
    <div class="hero">
      <div class="hero-greeting">Good morning, Radhika 👋</div>
      <div class="hero-label">Total portfolio value</div>
      <div class="hero-val" id="dash-total">AED 56,320</div>
      <div class="hero-change pos" id="dash-change">▲ +AED 1,240 (2.6%) this week</div>
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
      <div class="stat-card"><div class="sc-label">Total return</div><div class="sc-val pos" id="dash-return">+AED 6,820</div><div class="sc-sub pos">+13.8% overall</div></div>
      <div class="stat-card"><div class="sc-label">Cash balance</div><div class="sc-val" id="dash-cash" style="color:#d0e8d6">AED 12,400</div><div class="sc-sub neutral">Available to invest</div></div>
      <div class="stat-card"><div class="sc-label">Risk level</div><div class="sc-val warn">Medium</div><div class="sc-sub neutral">Score: 58/100</div></div>
    </div>
    <div class="sec-head">AI Insight</div>
    <div class="ai-card">
      <div class="ai-badge">Smart recommendation</div>
      <div class="ai-text">Your AAPL position is up 14%. Consider taking partial profits or diversifying into a stable bond ETF to reduce concentration risk in your portfolio.</div>
      <div class="ai-btns">
        <button class="ai-btn ab-hold">Hold</button>
        <button class="ai-btn ab-sell" onclick="switchTab('t-trade')">Sell</button>
        <button class="ai-btn ab-div" onclick="switchTab('t-rebal')">Rebalance</button>
      </div>
    </div>
    <div class="sec-head">Market Movers</div>
    <div class="h-row" onclick="switchTab('t-trade');selectStock('AAPL')">
      <div class="ticker t-bl">AAPL</div>
      <div class="h-info"><div class="h-name">Apple Inc.</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 824</div><div class="h-pct pos">▲ +1.4%</div></div>
    </div>
    <div class="h-row" onclick="switchTab('t-trade');selectStock('MSFT')">
      <div class="ticker t-gr">MSFT</div>
      <div class="h-info"><div class="h-name">Microsoft</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 1,260</div><div class="h-pct pos">▲ +0.8%</div></div>
    </div>
    <div class="h-row" onclick="switchTab('t-trade');selectStock('TSLA')">
      <div class="ticker t-am">TSLA</div>
      <div class="h-info"><div class="h-name">Tesla</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 612</div><div class="h-pct neg">▼ -2.1%</div></div>
    </div>
    <div class="h-row" onclick="switchTab('t-trade');selectStock('NVDA')">
      <div class="ticker t-pu">NVDA</div>
      <div class="h-info"><div class="h-name">NVIDIA</div><div class="h-sub">NASDAQ</div></div>
      <div class="h-right"><div class="h-val">AED 4,180</div><div class="h-pct pos">▲ +3.2%</div></div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- HOLDINGS -->
  <div class="scroll" id="tab-hold" style="display:none">
    <div style="padding:16px;background:#04120a">
      <div class="stat-card" style="margin-bottom:6px">
        <div class="sc-label">Total holdings value</div>
        <div class="sc-val" id="hold-total" style="font-size:24px;color:#d0e8d6">AED 56,320</div>
        <div class="sc-sub pos" id="hold-profit">+AED 6,820 total profit</div>
      </div>
    </div>
    <div class="sec-head">Your Positions</div>
    <div id="holdings-list"></div>
    <div style="padding:16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Portfolio Allocation</div>
      <div class="stat-card" id="alloc-wrap"></div>
    </div>
    <div style="padding:0 16px 16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Recent Activity</div>
      <div class="stat-card" id="activity-list">
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

  <!-- TRADE TAB -->
  <div class="scroll" id="tab-trade" style="display:none">
    <div class="hero" style="padding-bottom:14px">
      <div style="font-size:10px;color:#3a6647;text-transform:uppercase;letter-spacing:.4px;margin-bottom:3px">Stock Trading</div>
      <div style="font-size:22px;font-weight:700;color:#e0f0e6;margin-bottom:3px">Buy &amp; Sell Stocks</div>
      <div style="font-size:11px;color:#3a6647">UAE market hours: Sun–Thu 10:00 AM – 2:00 PM GST</div>
    </div>
    <div style="padding:12px 16px 0">
      <div style="font-size:10px;color:#3a6647;text-transform:uppercase;letter-spacing:.4px;margin-bottom:6px">Cash Balance</div>
      <div style="font-size:22px;font-weight:700;color:#2ecc71" id="trade-cash-display">AED 12,400.00</div>
    </div>
    <div class="trade-seg" id="trade-seg" style="margin-top:14px">
      <button class="trade-seg-btn active" onclick="setTradeMode('buy')">Buy</button>
      <button class="trade-seg-btn" onclick="setTradeMode('sell')">Sell</button>
    </div>
    <div class="stock-pick">
      <div class="stock-pick-label">Select Stock</div>
      <div class="stock-btn-row" id="stock-btn-row"></div>
    </div>
    <div class="trade-form">
      <div class="trade-stock-header">
        <div class="ticker t-bl" id="trade-ticker">AAPL</div>
        <div>
          <div style="font-size:14px;font-weight:700;color:#d0e8d6" id="trade-name">Apple Inc.</div>
          <div style="font-size:11px;color:#3a6647" id="trade-exchange">NASDAQ</div>
        </div>
        <div style="margin-left:auto;text-align:right">
          <div style="font-size:18px;font-weight:700;color:#2ecc71" id="trade-price">AED 824.50</div>
          <div style="font-size:10px;color:#2ecc71" id="trade-change-lbl">▲ +1.4% today</div>
        </div>
      </div>
      <div class="trade-price-row">
        <div><div class="trade-price-label">Bid</div><div class="trade-price-val" id="trade-bid">AED 823.80</div></div>
        <div><div class="trade-price-label">Ask</div><div class="trade-price-val" id="trade-ask">AED 825.20</div></div>
        <div><div class="trade-price-label">You own</div><div class="trade-price-val" id="trade-owned">12 shares</div></div>
      </div>
      <div class="qty-row">
        <label>Quantity</label>
        <button class="qty-btn" onclick="changeQty(-1)">−</button>
        <input class="qty-input" type="number" id="trade-qty" value="1" min="1" oninput="updateTradeSummary()">
        <button class="qty-btn" onclick="changeQty(1)">+</button>
      </div>
      <div class="trade-summary">
        <div class="trade-summary-row"><span style="color:#3a6647">Price per share</span><span id="ts-price" style="color:#d0e8d6">AED 824.50</span></div>
        <div class="trade-summary-row"><span style="color:#3a6647">Quantity</span><span id="ts-qty" style="color:#d0e8d6">1 share</span></div>
        <div class="trade-summary-row"><span style="color:#3a6647">Brokerage (0.1%)</span><span id="ts-fee" style="color:#d0e8d6">AED 0.82</span></div>
        <div class="trade-summary-row"><span style="color:#d0e8d6">Total</span><span id="ts-total" style="color:#2ecc71">AED 825.32</span></div>
      </div>
      <button class="btn-buy" id="trade-action-btn" onclick="executeTrade()">Buy AAPL</button>
    </div>
    <div class="sec-head" style="margin-top:4px">Recent Trades</div>
    <div style="margin:0 16px 20px">
      <div class="stat-card" id="trade-history">
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div><div style="font-size:13px;color:#d0e8d6">Bought AAPL</div><div style="font-size:10px;color:#3a6647;margin-top:2px">Apr 2, 2026 · 12 shares</div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#e74c3c">−AED 9,882</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0">
          <div><div style="font-size:13px;color:#d0e8d6">Sold TSLA</div><div style="font-size:10px;color:#3a6647;margin-top:2px">Mar 28, 2026 · 1 share</div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#2ecc71">+AED 636</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- REBALANCE TAB (dedicated) -->
  <div class="scroll" id="tab-rebal" style="display:none">
    <div class="hero" style="padding-bottom:16px">
      <div style="font-size:10px;color:#3a6647;text-transform:uppercase;letter-spacing:.4px;margin-bottom:3px">Portfolio Rebalancing</div>
      <div style="font-size:22px;font-weight:700;color:#e0f0e6;margin-bottom:3px">Rebalance</div>
      <div style="font-size:11px;color:#3a6647">Set target allocations and generate a rebalance plan</div>
    </div>

    <!-- Upload portfolio CSV -->
    <div style="padding:16px 16px 0">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Import Your Portfolio</div>
      <div class="upload-zone" id="upload-zone" onclick="triggerUpload()">
        <div style="font-size:24px;margin-bottom:8px">📂</div>
        <div style="font-size:13px;font-weight:700;color:#5a8a6a">Upload CSV / JSON</div>
        <div style="font-size:11px;color:#3a6647;margin-top:4px">Format: ticker, shares, avg_cost</div>
        <div style="font-size:10px;color:#1e4a2c;margin-top:6px">Or paste below to load a sample</div>
        <button class="upload-btn" onclick="loadSamplePortfolio(event)">Load sample portfolio</button>
        <input type="file" id="csv-upload" accept=".csv,.json" style="display:none" onchange="handleFileUpload(event)">
      </div>
      <div id="import-status" style="display:none;font-size:12px;color:#2ecc71;margin-bottom:10px;text-align:center;font-weight:700"></div>
    </div>

    <!-- Current vs Target -->
    <div style="padding:0 16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Current vs Target Allocation</div>
      <div class="rebal-card" style="margin:0 0 12px">
        <div style="font-size:12px;color:#5a8a6a;margin-bottom:14px;line-height:1.5">Drag sliders to set your ideal allocation. Target total must equal 100%.</div>
        <div id="rebal-rows-main"></div>
        <div style="border-top:1px solid #0f2a18;padding-top:12px;margin-top:4px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
            <div style="font-size:12px;color:#5a8a6a">Target total</div>
            <div style="font-size:14px;font-weight:700" id="rebal-total-pct2">100%</div>
          </div>
          <button onclick="applyRebalance2()" style="width:100%;background:#0a2a14;color:#2ecc71;border:1px solid #2ecc71;border-radius:11px;padding:11px;font-size:13px;font-weight:700;cursor:pointer">Generate Rebalance Plan</button>
        </div>
      </div>
    </div>

    <!-- Rebalance plan output -->
    <div id="rebal-plan2" style="display:none;padding:0 16px 16px">
      <div class="sec-head" style="padding:0;margin-bottom:9px">Rebalance Actions</div>
      <div class="stat-card" id="rebal-actions2"></div>
      <div style="background:rgba(243,156,18,.08);border:1px solid rgba(243,156,18,.2);border-radius:10px;padding:10px 14px;margin-top:10px">
        <div style="font-size:11px;color:#f39c12;font-weight:700;margin-bottom:4px">⚠ Disclaimer</div>
        <div style="font-size:10px;color:#8a6a3a;line-height:1.5">This is a suggestion only and does not constitute regulated financial advice. Consult a licensed financial advisor before making investment decisions.</div>
      </div>
    </div>
    <div style="height:24px"></div>
  </div>

  <!-- RISK -->
  <div class="scroll" id="tab-risk" style="display:none">
    <div class="hero" style="padding-bottom:16px">
      <div style="font-size:11px;color:#3a6647;margin-bottom:3px;text-transform:uppercase;letter-spacing:.4px">Portfolio Risk Score</div>
      <div style="font-size:30px;font-weight:700;color:#f39c12">58 / 100</div>
      <div style="font-size:12px;color:#3a6647;margin-top:4px">Based on your current holdings and market conditions</div>
    </div>
    <div style="padding:14px 16px 4px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Overall Risk Meter</div>
      <div class="risk-card" style="margin:0 0 14px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <div class="risk-title" style="margin-bottom:0">Your risk level</div>
          <div class="risk-badge" style="background:rgba(243,156,18,.13);color:#f39c12">Medium</div>
        </div>
        <div class="risk-meter">
          <div class="risk-fill" style="width:58%;background:linear-gradient(90deg,#2ecc71,#f39c12)"></div>
        </div>
        <div class="risk-labels"><span>Low</span><span>Medium</span><span>High</span></div>
        <div style="font-size:11px;color:#5a8a6a;margin-top:10px;line-height:1.5">Your portfolio has moderate risk. TSLA adds volatility while MSFT provides stability. Consider rebalancing to reduce single-stock concentration.</div>
      </div>
      <div class="sec-head" style="padding:0;margin-bottom:10px">Risk Simulator</div>
      <div class="risk-card" style="margin:0 0 14px">
        <div style="font-size:12px;color:#5a8a6a;margin-bottom:14px;line-height:1.5">Drag sliders to see how changes affect your risk score.</div>
        <div class="risk-sliders">
          <div class="risk-row"><label>AAPL weight</label><input type="range" min="0" max="80" value="50" step="1" oninput="updateRisk()" id="sl-aapl"><span id="v-aapl" style="color:#3498db">50%</span></div>
          <div class="risk-row"><label>MSFT weight</label><input type="range" min="0" max="80" value="33" step="1" oninput="updateRisk()" id="sl-msft"><span id="v-msft" style="color:#2ecc71">33%</span></div>
          <div class="risk-row"><label>TSLA weight</label><input type="range" min="0" max="80" value="17" step="1" oninput="updateRisk()" id="sl-tsla"><span id="v-tsla" style="color:#f39c12">17%</span></div>
          <div class="risk-row"><label>Bonds / ETFs</label><input type="range" min="0" max="80" value="0" step="1" oninput="updateRisk()" id="sl-bond"><span id="v-bond" style="color:#5a8a6a">0%</span></div>
        </div>
        <div style="margin-top:12px;border-top:1px solid #0f2a18;padding-top:12px">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <div style="font-size:12px;color:#5a8a6a">Simulated risk score</div>
            <div style="font-size:18px;font-weight:700" id="sim-score" class="warn">58</div>
          </div>
          <div class="risk-meter" style="margin-top:8px"><div class="risk-fill" id="sim-fill" style="width:58%;background:linear-gradient(90deg,#2ecc71,#f39c12)"></div></div>
          <div style="font-size:11px;color:#3a6647;margin-top:6px" id="sim-tip">Add bonds or reduce TSLA to lower your risk.</div>
        </div>
      </div>
      <div class="sec-head" style="padding:0;margin-bottom:10px">Risk By Holding</div>
      <div class="stat-card" style="margin-bottom:14px">
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-bl" style="width:32px;height:32px;font-size:9px">AAPL</div><div><div style="font-size:13px;color:#d0e8d6">Apple</div><div style="font-size:10px;color:#3a6647">Beta: 1.2</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#f39c12">Medium</div><div style="font-size:10px;color:#3a6647">50% of portfolio</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-gr" style="width:32px;height:32px;font-size:9px">MSFT</div><div><div style="font-size:13px;color:#d0e8d6">Microsoft</div><div style="font-size:10px;color:#3a6647">Beta: 0.9</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#2ecc71">Low</div><div style="font-size:10px;color:#3a6647">33% of portfolio</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #0f2a18">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-am" style="width:32px;height:32px;font-size:9px">TSLA</div><div><div style="font-size:13px;color:#d0e8d6">Tesla</div><div style="font-size:10px;color:#3a6647">Beta: 2.1</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#e74c3c">High</div><div style="font-size:10px;color:#3a6647">17% of portfolio</div></div>
        </div>
        <div style="display:flex;justify-content:space-between;padding:10px 0">
          <div style="display:flex;align-items:center;gap:9px"><div class="ticker t-pi" style="width:32px;height:32px;font-size:9px">META</div><div><div style="font-size:13px;color:#d0e8d6">Meta</div><div style="font-size:10px;color:#3a6647">Beta: 1.5</div></div></div>
          <div style="text-align:right"><div style="font-size:12px;font-weight:700;color:#f39c12">Medium</div><div style="font-size:10px;color:#3a6647">17% of portfolio</div></div>
        </div>
      </div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- ESG -->
  <div class="scroll" id="tab-esg" style="display:none">
    <div class="esg-hero">
      <div style="font-size:11px;color:#3a6647;margin-bottom:4px;text-transform:uppercase;letter-spacing:.4px">Portfolio ESG Score</div>
      <div class="esg-big">72</div>
      <div style="font-size:12px;color:#3a6647;margin-top:4px">4 active holdings · Updated daily</div>
      <div class="esg-pill">Above UAE market average (64)</div>
    </div>
    <div style="padding:16px">
      <div class="sec-head" style="padding:0;margin-bottom:10px">Score Breakdown</div>
      <div class="esg-item"><div style="display:flex;justify-content:space-between"><span style="font-size:13px;font-weight:700;color:#d0e8d6">Environmental</span><span style="font-size:13px;font-weight:700;color:#2ecc71">72</span></div><div class="esg-bar-bg"><div class="esg-bar" style="width:72%;background:#2ecc71"></div></div><div style="font-size:11px;color:#3a6647;margin-top:6px">Low carbon footprint. MSFT leads with carbon-neutral operations.</div></div>
      <div class="esg-item"><div style="display:flex;justify-content:space-between"><span style="font-size:13px;font-weight:700;color:#d0e8d6">Social</span><span style="font-size:13px;font-weight:700;color:#3498db">65</span></div><div class="esg-bar-bg"><div class="esg-bar" style="width:65%;background:#3498db"></div></div><div style="font-size:11px;color:#3a6647;margin-top:6px">Fair labour practices. META scores lower on platform safety.</div></div>
      <div class="esg-item"><div style="display:flex;justify-content:space-between"><span style="font-size:13px;font-weight:700;color:#d0e8d6">Governance</span><span style="font-size:13px;font-weight:700;color:#f39c12">80</span></div><div class="esg-bar-bg"><div class="esg-bar" style="width:80%;background:#f39c12"></div></div><div style="font-size:11px;color:#3a6647;margin-top:6px">Strong board structure and financial transparency.</div></div>
      <div class="sec-head" style="padding:0;margin:14px 0 10px">Holdings ESG Rating</div>
      <div class="stat-card">
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #0f2a18"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-gr" style="width:30px;height:30px;font-size:9px">MSFT</div><span style="font-size:13px;color:#d0e8d6">Microsoft</span></div><span style="color:#2ecc71;font-weight:700;font-size:13px">85 / AA</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #0f2a18"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-bl" style="width:30px;height:30px;font-size:9px">AAPL</div><span style="font-size:13px;color:#d0e8d6">Apple</span></div><span style="color:#2ecc71;font-weight:700;font-size:13px">78 / A</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #0f2a18"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-am" style="width:30px;height:30px;font-size:9px">TSLA</div><span style="font-size:13px;color:#d0e8d6">Tesla</span></div><span style="color:#f39c12;font-weight:700;font-size:13px">54 / B</span></div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0"><div style="display:flex;align-items:center;gap:9px"><div class="ticker t-pi" style="width:30px;height:30px;font-size:9px">META</div><span style="font-size:13px;color:#d0e8d6">Meta</span></div><span style="color:#e74c3c;font-weight:700;font-size:13px">48 / C</span></div>
      </div>
      <div class="ai-card" style="margin:12px 0 0"><div class="ai-badge">ESG Tip</div><div class="ai-text">Replacing META with a higher-rated ESG alternative (e.g. clean energy ETF) could lift your Social score from 65 to ~73.</div></div>
    </div>
    <div style="height:20px"></div>
  </div>

  <!-- LEARN -->
  <div class="scroll" id="tab-learn" style="display:none">
    <div class="learn-hero">
      <div class="learn-hero-title">Learn</div>
      <div class="learn-hero-sub">Test your knowledge and look up key terms.</div>
      <div class="progress-bar-bg"><div class="progress-bar"></div></div>
    </div>
    <div style="padding:16px 0 4px">
      <div class="sec-head">Quick Quiz</div>
      <div class="quiz-card">
        <div style="font-size:10px;color:#3a6647;margin-bottom:8px" id="q-counter">Question 1 of 6</div>
        <div class="quiz-q" id="q-text">What does "diversification" mean in investing?</div>
        <div class="quiz-opts" id="q-opts"></div>
        <div class="quiz-result pos" id="q-result" style="font-size:12px;margin-top:10px;display:none"></div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px">
          <div style="font-size:11px;color:#3a6647" id="q-score">Score: 0 / 0</div>
          <button style="background:rgba(46,204,113,.12);color:#2ecc71;border:none;border-radius:8px;padding:7px 14px;font-size:11px;font-weight:700;cursor:pointer" onclick="nextQ()">Next →</button>
        </div>
      </div>
      <div class="sec-head" style="margin-top:8px">Key Terms Glossary</div>
      <div class="glossary-card"><div class="g-term">Bull Market</div><div class="g-def">A period when stock prices are rising (20%+ from lows). Investors are optimistic and confident.</div></div>
      <div class="glossary-card"><div class="g-term">Bear Market</div><div class="g-def">A period of falling prices (20%+ drop from highs). Can be a buying opportunity for long-term investors.</div></div>
      <div class="glossary-card"><div class="g-term">Dividend</div><div class="g-def">Cash payments companies send to shareholders, usually quarterly — a sign the company is profitable.</div></div>
      <div class="glossary-card"><div class="g-term">ETF</div><div class="g-def">A basket of stocks you buy as one investment — instant diversification. The S&amp;P 500 ETF holds 500 companies.</div></div>
      <div class="glossary-card"><div class="g-term">Beta</div><div class="g-def">Measures a stock's volatility vs the market. Beta &gt; 1 = more volatile (e.g. Tesla 2.1). Beta &lt; 1 = more stable.</div></div>
      <div class="glossary-card"><div class="g-term">P/E Ratio</div><div class="g-def">Price ÷ Earnings Per Share. Shows how much you pay for every AED 1 of profit.</div></div>
      <div class="glossary-card"><div class="g-term">Market Cap</div><div class="g-def">Total value of a company's shares. Share price × total shares outstanding.</div></div>
      <div class="glossary-card"><div class="g-term">Diversification</div><div class="g-def">Spreading investments across different assets so one bad pick doesn't sink your whole portfolio.</div></div>
    </div>
    <div style="height:24px"></div>
  </div>

  <!-- PROFILE -->
  <div class="scroll" id="tab-prof" style="display:none">
    <div class="prof-hero">
      <div class="prof-av">RS</div>
      <div class="prof-name">Radhika Sharma</div>
      <div class="prof-email">radhika@investiq.ae</div>
      <div class="prof-plan">Pro Plan · AED 49/mo</div>
    </div>
    <div style="padding-top:6px">
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="5" r="3" stroke="#2ecc71" stroke-width="1.2"/><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Account details</span></div><span class="mi-arrow">›</span></div>
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="3" width="12" height="10" rx="2" stroke="#2ecc71" stroke-width="1.2"/><path d="M5 7h6M5 10h4" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Subscription &amp; billing</span></div><span class="mi-arrow">›</span></div>
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2l1 3h3l-2.5 1.8 1 3L8 8.2 5.5 9.8l1-3L4 5h3z" stroke="#2ecc71" stroke-width="1.2" stroke-linejoin="round"/></svg></div><span class="mi-label">ESG preferences</span></div><span class="mi-arrow">›</span></div>
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="#2ecc71" stroke-width="1.2"/><path d="M8 5v4M8 11v.5" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Risk profile settings</span></div><span class="mi-arrow">›</span></div>
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2C5.8 2 4 3.8 4 6v3L2.5 11h11L12 9V6c0-2.2-1.8-4-4-4z" stroke="#2ecc71" stroke-width="1.2"/><path d="M6.5 13.5c0 .8.7 1.5 1.5 1.5s1.5-.7 1.5-1.5" stroke="#2ecc71" stroke-width="1.2"/></svg></div><span class="mi-label">Notifications</span></div><span class="mi-arrow">›</span></div>
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="2" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/><rect x="9" y="2" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/><rect x="2" y="9" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/><rect x="9" y="9" width="5" height="5" rx="1" stroke="#2ecc71" stroke-width="1.2"/></svg></div><span class="mi-label">Investor Academy</span></div><span class="mi-arrow">›</span></div>
      <div class="menu-item"><div class="mi-left"><div class="mi-icon"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 4h12M2 8h8M2 12h10" stroke="#2ecc71" stroke-width="1.2" stroke-linecap="round"/></svg></div><span class="mi-label">Help &amp; support</span></div><span class="mi-arrow">›</span></div>
    </div>
    <button class="logout-btn" onclick="show('s-login')">Sign out of InvestIQ</button>
    <div style="text-align:center;font-size:11px;color:#1a3a24;padding-bottom:20px">InvestIQ v2.1 · Dubai, UAE · Not regulated financial advice — prototype only.</div>
  </div>

  <!-- BOTTOM NAV -->
  <div class="nav-bar">
    <button class="nav-btn active" id="nb-dash" onclick="switchTab('t-dash')">
      <svg viewBox="0 0 20 20" fill="none"><rect x="1" y="10" width="5" height="8" rx="1" fill="currentColor"/><rect x="7.5" y="6" width="5" height="12" rx="1" fill="currentColor"/><rect x="14" y="2" width="5" height="16" rx="1" fill="currentColor"/></svg>Home
    </button>
    <button class="nav-btn" id="nb-hold" onclick="switchTab('t-hold')">
      <svg viewBox="0 0 20 20" fill="none"><rect x="2" y="2" width="16" height="16" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M6 10h8M6 13.5h5M6 6.5h8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>Holdings
    </button>
    <button class="nav-btn" id="nb-trade" onclick="switchTab('t-trade')">
      <svg viewBox="0 0 20 20" fill="none"><path d="M5 14l3-4 3 3 4-6" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="5" cy="14" r="1" fill="currentColor"/><circle cx="15" cy="7" r="1" fill="currentColor"/></svg>Trade
    </button>
    <button class="nav-btn" id="nb-rebal" onclick="switchTab('t-rebal')">
      <svg viewBox="0 0 20 20" fill="none"><path d="M3 10h14M10 3v14" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/><circle cx="10" cy="10" r="3" stroke="currentColor" stroke-width="1.4"/></svg>Rebalance
    </button>
    <button class="nav-btn" id="nb-risk" onclick="switchTab('t-risk')">
      <svg viewBox="0 0 20 20" fill="none"><path d="M10 2L2 17h16L10 2z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M10 8v4M10 14v.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>Risk
    </button>
    <button class="nav-btn" id="nb-learn" onclick="switchTab('t-learn')">
      <svg viewBox="0 0 20 20" fill="none"><path d="M10 3L2 7l8 4 8-4-8-4z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="M6 9v5a4 4 0 008 0V9" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>Learn
    </button>
    <button class="nav-btn" id="nb-prof" onclick="switchTab('t-prof')">
      <svg viewBox="0 0 20 20" fill="none"><circle cx="10" cy="7" r="3.5" stroke="currentColor" stroke-width="1.4"/><path d="M3 18c0-3.9 3.1-7 7-7s7 3.1 7 7" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>Profile
    </button>
  </div>
</div>

<!-- Toast -->
<div id="global-toast" class="trade-toast" style="position:absolute"></div>

</div>

<script>
var STOCKS={
  AAPL:{name:'Apple Inc.',price:824.50,change:'+1.4%',pos:true,owned:12,col:'t-bl',bid:823.80,ask:825.20,mkt:'NASDAQ',cost:722.20},
  MSFT:{name:'Microsoft Corp.',price:1260.00,change:'+0.8%',pos:true,owned:8,col:'t-gr',bid:1259.00,ask:1261.00,mkt:'NASDAQ',cost:1187.50},
  TSLA:{name:'Tesla Inc.',price:612.00,change:'-2.1%',pos:false,owned:5,col:'t-am',bid:611.20,ask:612.80,mkt:'NASDAQ',cost:636.40},
  META:{name:'Meta Platforms',price:2180.00,change:'+2.7%',pos:true,owned:3,col:'t-pi',bid:2179.00,ask:2181.00,mkt:'NASDAQ',cost:1993.00},
  AMZN:{name:'Amazon.com Inc.',price:3320.00,change:'+1.1%',pos:true,owned:0,col:'t-am',bid:3318.50,ask:3321.50,mkt:'NASDAQ',cost:3320.00},
  GOOGL:{name:'Alphabet Inc.',price:7050.00,change:'+0.5%',pos:true,owned:0,col:'t-bl',bid:7048.00,ask:7052.00,mkt:'NASDAQ',cost:7050.00},
  NVDA:{name:'NVIDIA Corp.',price:4180.00,change:'+3.2%',pos:true,owned:0,col:'t-pu',bid:4177.00,ask:4183.00,mkt:'NASDAQ',cost:4180.00},
  JPM:{name:'JPMorgan Chase',price:1745.00,change:'+0.4%',pos:true,owned:0,col:'t-bl',bid:1744.00,ask:1746.00,mkt:'NYSE',cost:1745.00},
  BAC:{name:'Bank of America',price:420.00,change:'-0.3%',pos:false,owned:0,col:'t-am',bid:419.50,ask:420.50,mkt:'NYSE',cost:420.00},
  NFLX:{name:'Netflix Inc.',price:5580.00,change:'+1.8%',pos:true,owned:0,col:'t-pi',bid:5578.00,ask:5582.00,mkt:'NASDAQ',cost:5580.00},
  BABA:{name:'Alibaba Group',price:980.00,change:'-0.9%',pos:false,owned:0,col:'t-am',bid:979.00,ask:981.00,mkt:'NYSE',cost:980.00},
  V:{name:'Visa Inc.',price:2640.00,change:'+0.6%',pos:true,owned:0,col:'t-gr',bid:2639.00,ask:2641.00,mkt:'NYSE',cost:2640.00},
  DIS:{name:'Walt Disney Co.',price:1050.00,change:'-0.5%',pos:false,owned:0,col:'t-bl',bid:1049.00,ask:1051.00,mkt:'NYSE',cost:1050.00},
  PYPL:{name:'PayPal Holdings',price:620.00,change:'-1.2%',pos:false,owned:0,col:'t-am',bid:619.00,ask:621.00,mkt:'NASDAQ',cost:620.00},
  UBER:{name:'Uber Technologies',price:475.00,change:'+2.1%',pos:true,owned:0,col:'t-gr',bid:474.20,ask:475.80,mkt:'NYSE',cost:475.00},
  SHOP:{name:'Shopify Inc.',price:1380.00,change:'+1.5%',pos:true,owned:0,col:'t-pi',bid:1379.00,ask:1381.00,mkt:'NYSE',cost:1380.00},
  EMAAR:{name:'Emaar Properties',price:18.40,change:'+0.8%',pos:true,owned:0,col:'t-gr',bid:18.35,ask:18.45,mkt:'DFM',cost:18.40},
  DIB:{name:'Dubai Islamic Bank',price:5.90,change:'+0.3%',pos:true,owned:0,col:'t-bl',bid:5.88,ask:5.92,mkt:'DFM',cost:5.90},
  ENBD:{name:'Emirates NBD',price:14.60,change:'-0.2%',pos:false,owned:0,col:'t-am',bid:14.55,ask:14.65,mkt:'DFM',cost:14.60},
  ADNOC:{name:'ADNOC Distribution',price:3.82,change:'+0.5%',pos:true,owned:0,col:'t-pi',bid:3.80,ask:3.84,mkt:'ADX',cost:3.82}
};

var tradeMode='buy';
var selStock='AAPL';
var availBal=12400;

var REBAL_COLS={AAPL:'t-bl',MSFT:'t-gr',TSLA:'t-am',META:'t-pi'};
var REBAL_COLORS={AAPL:'#3498db',MSFT:'#2ecc71',TSLA:'#f39c12',META:'#e91e8c'};
var rebalPortfolio={
  AAPL:{shares:12,price:824.50},
  MSFT:{shares:8,price:1260.00},
  TSLA:{shares:5,price:612.00},
  META:{shares:3,price:2180.00}
};

function show(id){document.querySelectorAll('.screen').forEach(function(s){s.classList.remove('active');});document.getElementById(id).classList.add('active');}

function doLogin(){
  var p=document.getElementById('l-pass').value;
  var e=document.getElementById('l-err');
  if(p==='demo1234'){e.style.display='none';runLoadingSequence(function(){show('s-app');switchTab('t-dash');});}
  else{e.style.display='block';}
}
function goApp(){runLoadingSequence(function(){show('s-app');switchTab('t-dash');});}
function runLoadingSequence(cb){
  show('s-loading');
  var bar=document.getElementById('load-bar');
  var title=document.getElementById('load-title');
  var sub=document.getElementById('load-sub');
  var steps=[{w:'15%',t:'Signing you in...',s:'Verifying credentials'},{w:'35%',t:'Signing you in...',s:'Authentication successful'},{w:'55%',t:'Loading your portfolio...',s:'Fetching holdings & prices'},{w:'72%',t:'Calculating insights...',s:'Running AI risk analysis'},{w:'88%',t:'Calculating insights...',s:'Preparing ESG scores'},{w:'100%',t:'Almost there...',s:'Building your dashboard'}];
  var i=0;
  function tick(){if(i>=steps.length){setTimeout(cb,300);return;}var s=steps[i];bar.style.width=s.w;title.textContent=s.t;sub.textContent=s.s;i++;setTimeout(tick,i===1?400:320);}
  tick();
}

var TAB_MAP={
  't-dash':['nb-dash','tab-dash'],
  't-hold':['nb-hold','tab-hold'],
  't-trade':['nb-trade','tab-trade'],
  't-rebal':['nb-rebal','tab-rebal'],
  't-risk':['nb-risk','tab-risk'],
  't-esg':['nb-esg','tab-esg'],
  't-learn':['nb-learn','tab-learn'],
  't-prof':['nb-prof','tab-prof']
};

function switchTab(id){
  document.querySelectorAll('.tab,.nav-btn').forEach(function(el){el.classList.remove('active');});
  Object.values(TAB_MAP).forEach(function(v){var c=document.getElementById(v[1]);if(c)c.style.display='none';});
  var tabEl=document.getElementById(id);
  if(tabEl)tabEl.classList.add('active');
  var map=TAB_MAP[id];
  if(map){
    var nb=document.getElementById(map[0]);if(nb)nb.classList.add('active');
    var tc=document.getElementById(map[1]);if(tc)tc.style.display='block';
  }
  if(id==='t-hold')renderHoldings();
}

function getPortfolioValue(){
  var total=0;
  Object.keys(STOCKS).forEach(function(sym){
    total+=STOCKS[sym].owned*STOCKS[sym].price;
  });
  return total;
}

function renderHoldings(){
  var list=document.getElementById('holdings-list');
  if(!list)return;
  list.innerHTML='';
  var costBasis=0;
  Object.keys(STOCKS).forEach(function(sym){
    var st=STOCKS[sym];
    if(st.owned<=0)return;
    var val=st.owned*st.price;
    var cost=st.owned*st.cost;
    costBasis+=cost;
    var pct=(st.price-st.cost)/st.cost*100;
    var row=document.createElement('div');
    row.className='h-row';
    row.innerHTML='<div class="ticker '+st.col+'">'+sym+'</div>'
      +'<div class="h-info"><div class="h-name">'+st.name+'</div><div class="h-sub">'+st.owned+' shares · AED '+st.price.toFixed(2)+'/sh</div></div>'
      +'<div class="h-right"><div class="h-val">AED '+val.toLocaleString('en-US',{maximumFractionDigits:0})+'</div>'
      +'<div class="h-pct '+(pct>=0?'pos':'neg')+'">'+(pct>=0?'▲ +':'▼ ')+pct.toFixed(1)+'%</div></div>';
    row.onclick=function(){selectStock(sym);switchTab('t-trade');};
    list.appendChild(row);
  });
  var portVal=getPortfolioValue();
  var totalVal=portVal+availBal;
  var profit=portVal-costBasis;
  document.getElementById('hold-total').textContent='AED '+portVal.toLocaleString('en-US',{maximumFractionDigits:0});
  document.getElementById('hold-profit').textContent=(profit>=0?'+':'')+' AED '+Math.abs(profit).toLocaleString('en-US',{maximumFractionDigits:0})+' total profit';
  renderAllocBars();
}

function renderAllocBars(){
  var aw=document.getElementById('alloc-wrap');
  if(!aw)return;
  aw.innerHTML='';
  var portVal=getPortfolioValue();
  var colors={AAPL:'#3498db',MSFT:'#2ecc71',TSLA:'#f39c12',META:'#e91e8c',NVDA:'#9b59b6',AMZN:'#f39c12',GOOGL:'#3498db'};
  Object.keys(STOCKS).forEach(function(sym){
    var st=STOCKS[sym];
    if(st.owned<=0)return;
    var val=st.owned*st.price;
    var pct=Math.round(val/portVal*100);
    var col=colors[sym]||'#2ecc71';
    aw.innerHTML+='<div style="margin-bottom:12px"><div style="display:flex;justify-content:space-between;font-size:12px;color:#5a8a6a;margin-bottom:4px"><span>'+sym+'</span><span>'+pct+'%</span></div><div style="height:5px;background:#0a2214;border-radius:3px;overflow:hidden"><div style="width:'+pct+'%;height:5px;background:'+col+';border-radius:3px"></div></div></div>';
  });
}

function buildStockBtns(){
  var row=document.getElementById('stock-btn-row');
  if(!row)return;
  row.innerHTML='';
  Object.keys(STOCKS).forEach(function(sym){
    var btn=document.createElement('button');
    btn.className='stock-btn'+(sym===selStock?' active':'');
    btn.textContent=sym;
    btn.onclick=function(){selectStock(sym);};
    row.appendChild(btn);
  });
}

function selectStock(sym){
  selStock=sym;
  document.querySelectorAll('.stock-btn').forEach(function(b){b.classList.toggle('active',b.textContent===sym);});
  var st=STOCKS[sym];
  document.getElementById('trade-ticker').textContent=sym;
  document.getElementById('trade-ticker').className='ticker '+st.col;
  document.getElementById('trade-name').textContent=st.name;
  document.getElementById('trade-exchange').textContent=st.mkt;
  document.getElementById('trade-price').textContent='AED '+st.price.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
  document.getElementById('trade-change-lbl').textContent=(st.pos?'▲ ':'▼ ')+st.change+' today';
  document.getElementById('trade-change-lbl').style.color=st.pos?'#2ecc71':'#e74c3c';
  document.getElementById('trade-bid').textContent='AED '+st.bid.toFixed(2);
  document.getElementById('trade-ask').textContent='AED '+st.ask.toFixed(2);
  document.getElementById('trade-owned').textContent=st.owned+' shares';
  document.getElementById('trade-qty').value=1;
  updateTradeSummary();
}

function setTradeMode(mode){
  tradeMode=mode;
  document.querySelectorAll('.trade-seg-btn').forEach(function(b,i){b.classList.toggle('active',i===(mode==='buy'?0:1));});
  var btn=document.getElementById('trade-action-btn');
  btn.className=mode==='buy'?'btn-buy':'btn-sell-red';
  updateTradeSummary();
}

function changeQty(d){
  var inp=document.getElementById('trade-qty');
  inp.value=Math.max(1,parseInt(inp.value||1)+d);
  updateTradeSummary();
}

function updateTradeSummary(){
  var st=STOCKS[selStock];
  var qty=Math.max(1,parseInt(document.getElementById('trade-qty').value)||1);
  var price=tradeMode==='buy'?st.ask:st.bid;
  var fee=price*qty*0.001;
  var total=tradeMode==='buy'?price*qty+fee:price*qty-fee;
  document.getElementById('ts-price').textContent='AED '+price.toFixed(2);
  document.getElementById('ts-qty').textContent=qty+' share'+(qty>1?'s':'');
  document.getElementById('ts-fee').textContent='AED '+fee.toFixed(2);
  document.getElementById('ts-total').textContent='AED '+total.toFixed(2);
  document.getElementById('ts-total').style.color=tradeMode==='buy'?'#e74c3c':'#2ecc71';
  document.getElementById('trade-cash-display').textContent='AED '+availBal.toLocaleString('en-US',{minimumFractionDigits:2});
  var btn=document.getElementById('trade-action-btn');
  btn.textContent=(tradeMode==='buy'?'Buy ':'Sell ')+qty+' '+selStock+(qty>1?' shares':' share');
}

function executeTrade(){
  var st=STOCKS[selStock];
  var qty=Math.max(1,parseInt(document.getElementById('trade-qty').value)||1);
  var price=tradeMode==='buy'?st.ask:st.bid;
  var fee=price*qty*0.001;
  var total=tradeMode==='buy'?price*qty+fee:price*qty-fee;
  if(tradeMode==='sell'&&qty>st.owned){showToast('Not enough shares to sell.',true);return;}
  if(tradeMode==='buy'&&total>availBal){showToast('Insufficient balance.',true);return;}
  if(tradeMode==='buy'){
    var oldCost=st.owned*st.cost;
    st.owned+=qty;
    st.cost=(oldCost+qty*st.ask)/st.owned;
    availBal-=total;
  }else{
    st.owned-=qty;
    availBal+=total;
  }
  document.getElementById('trade-owned').textContent=st.owned+' shares';
  document.getElementById('trade-cash-display').textContent='AED '+availBal.toLocaleString('en-US',{minimumFractionDigits:2});
  document.getElementById('dash-cash').textContent='AED '+Math.round(availBal).toLocaleString();
  document.getElementById('trade-qty').value=1;
  updateTradeSummary();
  showToast((tradeMode==='buy'?'Bought ':'Sold ')+qty+' '+selStock+' · AED '+total.toFixed(2),tradeMode==='sell');
  addTradeHistory((tradeMode==='buy'?'Bought':'Sold'),selStock,qty,total,tradeMode);
  buildRebalRows();
}

function showToast(msg,isSell){
  var t=document.getElementById('global-toast');
  t.textContent=msg;
  t.className='trade-toast'+(isSell?' sell-toast':'');
  t.style.display='block';
  setTimeout(function(){t.style.display='none';},2800);
}

function addTradeHistory(action,sym,qty,total,mode){
  var hist=document.getElementById('trade-history');
  var row=document.createElement('div');
  row.style.cssText='display:flex;justify-content:space-between;padding:10px 0;border-top:1px solid #0f2a18';
  var today=new Date().toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'});
  row.innerHTML='<div><div style="font-size:13px;color:#d0e8d6">'+action+' '+sym+'</div><div style="font-size:10px;color:#3a6647;margin-top:2px">'+today+' · '+qty+' share'+(qty>1?'s':'')+'</div></div>'
    +'<div style="text-align:right"><div style="font-size:12px;font-weight:700;color:'+(mode==='buy'?'#e74c3c':'#2ecc71')+'">'+(mode==='buy'?'−':'+')+'AED '+total.toFixed(2)+'</div></div>';
  hist.insertBefore(row,hist.firstChild);
}

function buildRebalRows(){
  var container=document.getElementById('rebal-rows-main');
  if(!container)return;
  container.innerHTML='';
  var portVal=0;
  Object.keys(rebalPortfolio).forEach(function(sym){
    portVal+=rebalPortfolio[sym].shares*STOCKS[sym].price;
  });
  Object.keys(rebalPortfolio).forEach(function(sym){
    var val=rebalPortfolio[sym].shares*STOCKS[sym].price;
    var curPct=Math.round(val/portVal*100);
    var col=REBAL_COLS[sym]||'t-gr';
    var color=REBAL_COLORS[sym]||'#2ecc71';
    var row=document.createElement('div');
    row.style.marginBottom='14px';
    row.innerHTML='<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">'
      +'<div class="rebal-ticker '+col+'" style="width:36px;height:36px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:9px;font-weight:700">'+sym+'</div>'
      +'<div style="flex:1">'
        +'<div style="display:flex;justify-content:space-between;font-size:10px;color:#3a6647;margin-bottom:3px">'
          +'<span>'+sym+' · Current: '+curPct+'%</span><span id="rt2-'+sym+'">Target: '+curPct+'%</span>'
        +'</div>'
        +'<div style="height:6px;background:#0a2214;border-radius:3px;position:relative;overflow:visible">'
          +'<div id="rc2-'+sym+'" style="height:6px;border-radius:3px;background:'+color+';width:'+curPct+'%"></div>'
        +'</div>'
        +'<div style="display:flex;align-items:center;gap:8px;margin-top:6px">'
          +'<label style="font-size:10px;color:#3a6647;width:55px;flex-shrink:0">Target %</label>'
          +'<input type="range" min="0" max="80" value="'+curPct+'" step="1" id="rs2-'+sym+'" oninput="updateRebal2(\''+sym+'\')" style="flex:1;accent-color:'+color+'">'
          +'<span id="rsv2-'+sym+'" style="font-size:11px;font-weight:700;color:'+color+';width:30px;text-align:right">'+curPct+'%</span>'
        +'</div>'
      +'</div>'
    +'</div>';
    container.appendChild(row);
  });
  updateRebalTotal2();
}

function updateRebal2(sym){
  var val=parseInt(document.getElementById('rs2-'+sym).value);
  document.getElementById('rsv2-'+sym).textContent=val+'%';
  document.getElementById('rt2-'+sym).textContent='Target: '+val+'%';
  updateRebalTotal2();
}

function updateRebalTotal2(){
  var tot=0;
  Object.keys(rebalPortfolio).forEach(function(s){
    var el=document.getElementById('rs2-'+s);
    if(el)tot+=parseInt(el.value);
  });
  var el=document.getElementById('rebal-total-pct2');
  if(el){el.textContent=tot+'%';el.style.color=tot===100?'#2ecc71':tot>100?'#e74c3c':'#f39c12';}
}

function applyRebalance2(){
  var portVal=0;
  Object.keys(rebalPortfolio).forEach(function(sym){portVal+=rebalPortfolio[sym].shares*STOCKS[sym].price;});
  var actions=[];
  Object.keys(rebalPortfolio).forEach(function(sym){
    var el=document.getElementById('rs2-'+sym);
    if(!el)return;
    var targetPct=parseInt(el.value)/100;
    var targetVal=portVal*targetPct;
    var curVal=rebalPortfolio[sym].shares*STOCKS[sym].price;
    var diff=targetVal-curVal;
    var shares=Math.round(Math.abs(diff)/STOCKS[sym].price);
    if(shares>0)actions.push({sym:sym,action:diff>0?'Buy':'Sell',shares:shares,value:Math.abs(diff).toFixed(0),col:diff>0?'#2ecc71':'#e74c3c',tickCol:REBAL_COLS[sym]||'t-gr'});
  });
  var plan=document.getElementById('rebal-plan2');
  var actEl=document.getElementById('rebal-actions2');
  plan.style.display='block';
  if(!actions.length){
    actEl.innerHTML='<div style="padding:14px;text-align:center;font-size:13px;color:#2ecc71;font-weight:700">Portfolio is already balanced!</div>';
    return;
  }
  var totalTrades=actions.reduce(function(a,b){return a+parseFloat(b.value);},0);
  actEl.innerHTML='<div style="display:flex;justify-content:space-between;padding:8px 12px;font-size:10px;color:#3a6647;border-bottom:1px solid #0f2a18"><span>Stock</span><span>Action</span><span>Est. Value</span></div>'
    +actions.map(function(a){
      return '<div style="display:flex;justify-content:space-between;align-items:center;padding:11px 12px;border-bottom:1px solid #071a0e">'
        +'<div style="display:flex;align-items:center;gap:8px"><div class="ticker '+a.tickCol+'" style="width:30px;height:30px;font-size:8px">'+a.sym+'</div><span style="font-size:13px;color:#d0e8d6">'+a.sym+'</span></div>'
        +'<span style="font-size:12px;font-weight:700;color:'+a.col+'">'+a.action+' '+a.shares+' share'+(a.shares>1?'s':'')+'</span>'
        +'<span style="font-size:12px;color:'+a.col+'">AED '+parseInt(a.value).toLocaleString()+'</span>'
        +'</div>';
    }).join('')
    +'<div style="padding:10px 12px;display:flex;justify-content:space-between;font-size:11px">'
      +'<span style="color:#3a6647">'+actions.length+' trade'+(actions.length>1?'s':'')+' needed</span>'
      +'<span style="color:#5a8a6a">Total: AED '+Math.round(totalTrades).toLocaleString()+'</span>'
    +'</div>';
}

function loadSamplePortfolio(e){
  e.stopPropagation();
  rebalPortfolio={
    AAPL:{shares:15,price:824.50},
    MSFT:{shares:6,price:1260.00},
    TSLA:{shares:8,price:612.00},
    META:{shares:2,price:2180.00}
  };
  document.getElementById('import-status').style.display='block';
  document.getElementById('import-status').textContent='Sample portfolio loaded — 4 positions imported';
  buildRebalRows();
}

function triggerUpload(){document.getElementById('csv-upload').click();}

function handleFileUpload(e){
  var file=e.target.files[0];
  if(!file)return;
  var reader=new FileReader();
  reader.onload=function(ev){
    var text=ev.target.result;
    var lines=text.split('\n').filter(function(l){return l.trim();});
    var newPortfolio={};
    lines.forEach(function(line,i){
      if(i===0&&line.toLowerCase().includes('ticker'))return;
      var parts=line.split(',');
      if(parts.length<2)return;
      var sym=parts[0].trim().toUpperCase();
      var shares=parseFloat(parts[1]);
      if(STOCKS[sym]&&!isNaN(shares)&&shares>0){
        newPortfolio[sym]={shares:shares,price:STOCKS[sym].price};
      }
    });
    if(Object.keys(newPortfolio).length>0){
      rebalPortfolio=newPortfolio;
      document.getElementById('import-status').style.display='block';
      document.getElementById('import-status').textContent='Imported '+Object.keys(newPortfolio).length+' positions from '+file.name;
      buildRebalRows();
    }else{
      document.getElementById('import-status').style.display='block';
      document.getElementById('import-status').style.color='#e74c3c';
      document.getElementById('import-status').textContent='Could not parse file. Use format: TICKER,SHARES,COST';
    }
  };
  reader.readAsText(file);
}

var RISK_BETA={aapl:1.2,msft:0.9,tsla:2.1,bond:0.2};
function updateRisk(){
  var w={aapl:parseInt(document.getElementById('sl-aapl').value),msft:parseInt(document.getElementById('sl-msft').value),tsla:parseInt(document.getElementById('sl-tsla').value),bond:parseInt(document.getElementById('sl-bond').value)};
  document.getElementById('v-aapl').textContent=w.aapl+'%';
  document.getElementById('v-msft').textContent=w.msft+'%';
  document.getElementById('v-tsla').textContent=w.tsla+'%';
  document.getElementById('v-bond').textContent=w.bond+'%';
  var total=w.aapl+w.msft+w.tsla+w.bond||1;
  var score=(w.aapl/total*RISK_BETA.aapl+w.msft/total*RISK_BETA.msft+w.tsla/total*RISK_BETA.tsla+w.bond/total*RISK_BETA.bond);
  var pct=Math.min(Math.round(score/2.1*100),100);
  var el=document.getElementById('sim-score');
  var fill=document.getElementById('sim-fill');
  var tip=document.getElementById('sim-tip');
  el.textContent=pct;
  fill.style.width=pct+'%';
  if(pct<35){el.className='pos';fill.style.background='#2ecc71';tip.textContent='Low risk — great for capital preservation.';}
  else if(pct<65){el.className='warn';fill.style.background='linear-gradient(90deg,#2ecc71,#f39c12)';tip.textContent='Balanced risk. Good mix for moderate growth.';}
  else{el.className='neg';fill.style.background='linear-gradient(90deg,#f39c12,#e74c3c)';tip.textContent='High risk! Consider adding bonds or stable stocks.';}
}

var QS=[
  {q:"What does 'diversification' mean in investing?",opts:["Putting all your money in one company","Spreading money across different investments to reduce risk","Only investing in bonds","Selling stocks when prices drop"],a:1},
  {q:"What does a high P/E ratio suggest about a stock?",opts:["The company is losing money","Investors have high growth expectations","The stock is cheap","The company pays large dividends"],a:1},
  {q:"What is 'Beta' in stock analysis?",opts:["The stock's dividend yield","A measure of a stock's volatility vs the market","The company's profit margin","The annual return of a stock"],a:1},
  {q:"What does ESG stand for?",opts:["Earnings, Sales, Growth","Environmental, Social, Governance","Equity, Stocks, Gold","Earnings, Shares, Gains"],a:1},
  {q:"What is a Bull Market?",opts:["Prices falling 20%+ from highs","A market with no volatility","Prices rising 20%+ from lows","A market only for bonds"],a:2},
  {q:"What does an ETF give you?",opts:["Ownership of one company","A fixed interest payment","Exposure to a basket of stocks","A guaranteed return"],a:2}
];
var qi=0,correctCount=0,answered=0;
function loadQ(){
  var q=QS[qi%QS.length];
  var c=document.getElementById('q-counter');if(c)c.textContent='Question '+(qi%QS.length+1)+' of '+QS.length;
  document.getElementById('q-text').textContent=q.q;
  var opts=document.getElementById('q-opts');opts.innerHTML='';
  var res=document.getElementById('q-result');if(res){res.style.display='none';}
  q.opts.forEach(function(o,i){var d=document.createElement('div');d.className='quiz-opt';d.textContent=o;d.onclick=function(){answerQ(d,i===q.a);};opts.appendChild(d);});
}
function answerQ(el,correct){
  document.querySelectorAll('.quiz-opt').forEach(function(o){o.onclick=null;o.style.opacity='.5';});
  el.style.opacity='1';el.classList.add(correct?'correct':'wrong');
  answered++;if(correct)correctCount++;
  var res=document.getElementById('q-result');
  if(res){res.style.display='block';if(correct){res.textContent='Correct! 🎉';res.style.color='#2ecc71';}else{res.textContent='Not quite — correct answer shown.';res.style.color='#e74c3c';document.querySelectorAll('.quiz-opt')[QS[qi%QS.length].a].classList.add('correct');document.querySelectorAll('.quiz-opt')[QS[qi%QS.length].a].style.opacity='1';}}
  var sc=document.getElementById('q-score');if(sc)sc.textContent='Score: '+correctCount+' / '+answered;
}
function nextQ(){qi++;loadQ();}

document.querySelectorAll('.tf').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.tf').forEach(function(x){x.classList.remove('active');});this.classList.add('active');});});

buildStockBtns();
buildRebalRows();
loadQ();
renderAllocBars();
selectStock('AAPL');
</script>
</body>
</html>
