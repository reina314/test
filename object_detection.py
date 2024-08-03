<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<html xmlns:v>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<meta charset="utf-8" />
<meta HTTP-EQUIV="Pragma" CONTENT="no-cache">
<meta HTTP-EQUIV="Expires" CONTENT="-1">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<link rel="icon" href="images/favicon.png">
<title>ASUS Wireless Router TUF GAMING AX4200 - エラーメッセージ</title>
<script type="text/JavaScript" src="/js/jquery.js"></script>
<style>
body{
color:#FFF;
font-family: Arial, MS UI Gothic, MS P Gothic, Microsoft Yahei UI, sans-serif;
}
.wrapper{
background:url(images/New_ui/login_bg.png) #1F1F1F no-repeat;
background-size: 1280px 1076px;
background-position: center 0%;
margin: 0px;
background:#283437\9;
}
.title_name {
font-size: 2.5em;
color:#93D2D9;
}
.title_text{
width:520px;
}
.prod_madelName{
font-size: 26pt;
color:#fff;
margin-left:78px;
margin-top: 10px;
}
.login_img{
width:43px;
height:43px;
background-image: url('images/New_ui/icon_titleName.png');
background-repeat: no-repeat;
}
.p1{
font-size: 16pt;
color:#fff;
width:480px;
}
.button{
background-color:#279FD9;
/*background:rgba(255,255,255,0.1);
border: solid 1px #6e8385;*/
border-radius: 4px ;
transition: visibility 0s linear 0.218s,opacity 0.218s,background-color 0.218s;
height: 68px;
width: 300px;
/*width: 220px;*/
font-size: 20pt;
color:#fff;
text-align: center;
float:right;
margin:25px 0 0 78px;
line-height:68px;
}
.form_input{
background-color:rgba(255,255,255,0.2);
background-color:#576D73\9;
border-radius: 4px;
padding:26px 22px;
width: 480px;
border: 0;
height:25px;
color:#fff;
color:#000\9; /* IE6 IE7 IE8 */
font-size:28px
}
.nologin{
margin:10px 0px 0px 78px;
background-color:rgba(255,255,255,0.2);
background-color:#576D73\9;
padding:20px;
line-height:36px;
border-radius: 5px;
width: 480px;
border: 0;
color:#fff;
font-size:28px;
}
.div_table{
display:table;
}
.div_tr{
display:table-row;
}
.div_td{
display:table-cell;
}
.title_gap{
margin:10px 0px 0px 78px;
}
.img_gap{
padding-right:30px;
vertical-align:middle;
}
.password_gap{
margin:30px 0px 0px 78px;
}
.error_hint{
color: rgb(255, 204, 0);
margin:10px 0px -10px 78px;
font-size: 18px;
font-weight: bolder;
}
.main_field_gap{
margin:100px auto 0;
}
ul{
margin: 0;
}
li{
margin: 10px 0;
}
#wanLink{
cursor: pointer;
}
.button_background{
background-color: transparent;
}
.connect{
-webkit-animation: connecting 3s infinite linear;
-moz-animation: connecting 3s infinite linear;
-o-animation: connecting 3s infinite linear;
animation: connecting 3s infinite linear;
}
/*for mobile device*/
@media screen and (max-width: 1000px){
.title_name {
font-size: 1.2em;
color:#93d2d9;
margin-left:15px;
}
.prod_madelName{
font-size: 1.2em;
margin-left: 15px;
}
.p1{
font-size: 12pt;
width:100%;
}
.login_img{
background-size: 75%;
}
.title_text{
width: 100%;
}
.form_input{
padding:13px 11px;
width: 100%;
height:25px;
font-size:16px
}
.button{
height: 50px;
width: 100%;
font-size: 14pt;
text-align: center;
float:right;
margin: 25px -30px 0 0;
line-height:50px;
padding: 0 10px;
}
.nologin{
margin-left:10px;
padding:10px;
line-height:18px;
width: 100%;
font-size:14px;
}
.error_hint{
margin-left:10px;
}
.main_field_gap{
width:80%;
margin:30px 0 0 15px;
/*margin:30px auto 0;*/
}
.title_gap{
margin-left:15px;
}
.password_gap{
margin-left:15px;
}
.img_gap{
padding-right:0;
vertical-align:middle;
}
ul{
margin-left:-20px;
}
li{
margin: 10px 0;
}
.connect{
-webkit-animation: connecting 3s infinite linear;
-moz-animation: connecting 3s infinite linear;
-o-animation: connecting 3s infinite linear;
animation: connecting 3s infinite linear;
}
}
@keyframes connecting {
0% {
left: 30px;
}
50% {
left: 220px;
}
100% {
left: 30px;
}
}
.model_img{
width: 120px;
height: 142px;
background: url('images/Model_product.png') no-repeat;
background-size: 100%;
}
.mode_img_COD{
width: 120px;
height: 142px;
background: url('images/Model_product_COD.png') no-repeat;
background-size: 100%;
}
</style>
<script type="text/javascript">
var casenum = '1';
var sw_mode = '1';
var wlc_psta = '0';
var wlc_express = '0';
if( ((sw_mode == 2 || sw_mode == 3) && wlc_psta == 1) || (sw_mode == 3 && wlc_psta == 3))
sw_mode = 4;
if(sw_mode == 3 && wlc_psta == 2)
sw_mode = 2;
var wanstate = -1;
var wansbstate = -1;
var wanauxstate = -1;
wanstate = 4;
wansbstate = 3;
wanauxstate = 1;

var isRCSupport = function(_ptn){return ('mssid 2.4G 5G update usbX1 rawifi switchctrl manual_stb 11AC 11AX mbo ofdma wpa3 pwrctrl smart_connect wbmenu tuf reboot_schedule ipv6 ipv6pt s46 PARENTAL2 dnsfilter dnspriv dualwan pptpd openvpnd utf8_ssid printer modem webdav rrsut cloudsync media appnet hdspindown diskutility dnssec usb_bk frs_feedback dblog email findasus atf bwdpi wrs_wbl ookla HTTPS letsencrypt ssh vpnc vpn_fusion repeater psta vht160 wps_multiband user_low_rssi tcode usericon cfg_wps_btn stainfo realip lacp wanbonding alexa ipsec_srv mumimo_5g mumimo_2g qam256_2g qam1024_5g netool cfg_sync fupgrade afwupg betaupg revertfw amas conndiag eula proxysta mtk account_binding gameMode wireguard ftp_ssl acl96'.search(_ptn) == -1) ? false : true;}
var tmo_support = isRCSupport("tmo");
function isSupport(_ptn){
var ui_support = [{ "mssid": 1, "2.4G": 1, "5G": 1, "update": 1, "usbX1": 1, "rawifi": 1, "switchctrl": 1, "manual_stb": 1, "11AC": 1, "11AX": 1, "mbo": 1, "ofdma": 1, "wpa3": 1, "pwrctrl": 1, "smart_connect": 1, "wbmenu": 1, "tuf": 1, "reboot_schedule": 1, "ipv6": 1, "ipv6pt": 1, "s46": 2, "PARENTAL2": 1, "dnsfilter": 2, "dnspriv": 1, "dualwan": 1, "pptpd": 1, "openvpnd": 1, "utf8_ssid": 1, "printer": 1, "modem": 1, "webdav": 1, "rrsut": 1, "cloudsync": 1, "media": 1, "appnet": 1, "hdspindown": 1, "diskutility": 1, "dnssec": 1, "usb_bk": 1, "frs_feedback": 2, "dblog": 1, "email": 1, "findasus": 1, "atf": 1, "bwdpi": 2, "wrs_wbl": 1, "ookla": 1, "HTTPS": 1, "letsencrypt": 1, "ssh": 1, "vpnc": 1, "vpn_fusion": 1, "repeater": 1, "psta": 1, "vht160": 1, "wps_multiband": 1, "user_low_rssi": 1, "tcode": 1, "usericon": 2, "cfg_wps_btn": 1, "stainfo": 1, "realip": 1, "lacp": 1, "wanbonding": 1, "alexa": 1, "ipsec_srv": 4, "mumimo_5g": 1, "mumimo_2g": 1, "qam256_2g": 1, "qam1024_5g": 1, "netool": 1, "cfg_sync": 1, "fupgrade": 1, "afwupg": 1, "betaupg": 1, "revertfw": 1, "amas": 1, "conndiag": 2, "eula": 1, "proxysta": 1, "mtk": 1, "account_binding": 2, "gameMode": 1, "wireguard": 1, "ftp_ssl": 1, "acl96": 1, "dpi_mals": 1, "dpi_vp": 1, "dpi_cc": 1, "adaptive_qos": 1, "traffic_analyzer": 1, "webs_filter": 1, "apps_filter": 1, "web_history": 1, "bandwidth_monitor": 1, "aicloudipk": 0, "concurrep": 0, "rp_express_2g": 0, "rp_express_5g": 0, "hnd": 0, "localap": 1, "nwtool": 1, "usbPortMax": 1, "usbX": 1, "usb3": 1, "wl_mfp": 0, "wlopmode": 0, "yadns": 0, "noRouter": 0, "RPMesh": 0, "odm": 0, "dualband": 1, "triband": 0, "quadband": 0, "separate_ssid": 0, "mssid_count": 3, "dhcp_static_dns": 1, "AWV_ookla": 2, "wanMax": 2, "open_nat": 1, "uu_accel": 0, "amas_wgn": 1, "internetctrl": 1, "AWV_dpi_cc": 1, "AWV_dpi_vp": 1, "AWV_dpi_mals": 1, "force_roaming": 1, "sta_ap_bind": 1, "re_reconnect": 1, "amas_eap": 1, "del_client_data": 1, "captcha": 2, "ledg": 0, "AWV_ledg": 0, "ledg_count": 0, "AWV_vpnc": 2, "AWV_vpns": 2, "noFwManual": 0, "noupdate": 0, "WL_SCHED_V2": 1, "WL_SCHED_V3": 2, "PC_SCHED_V3": 3, "wpa3rp": 1, "led_ctrl_cap": 0, "mobile_game_mode": 1, "Instant_Guard": 4, "MaxRule_bwdpi_wrs": 64, "MaxRule_parentctrl": 64, "MaxRule_PC_DAYTIME": 256, "PC_REWARD": 1, "MaxRule_extend_limit": 128, "MaxLen_http_name": 32, "MaxLen_http_passwd": 32, "CHPASS": 1, "MaxRule_VPN_FUSION_Conn": 2, "amasRouter": 1, "amasNode": 1, "inadyn": 1, "NEW_PHYMAP": 1, "FAMILY_GROUP": 1, "google_asst": 1, "nt_center": 4, "nt_center_ui": 0, "wps_method_ob": 1, "qis_hide_he_features": 1, "cobrand_change": 0, "wlband": 1, "profile_sync": 1, "CN_Boost": 0, "5g1_dfs": 0, "5g2_dfs": 0 }
][0];
return (ui_support[_ptn]) ? ui_support[_ptn] : 0;
}
var dsl_support = isSupport("dsl");
var gobi_support = isSupport("gobi");
var odm_support = isSupport("odm");
var wans_dualwan_orig = 'wan none';
var wans_flag = (wans_dualwan_orig.search("none") == -1) ? 1 : 0;
if(wans_dualwan_orig.search(" ") == -1)
wans_flag = 0;
var new_lan_ip = [{next_lanip: '172.25.11.254'}][0].next_lanip;
var header_info = [{ "host": "www.asusrouter.com", "current_page": "error_page.htm", "protocol": "http", "port": 80 }];
var location_org = header_info[0].protocol + "://" + header_info[0].host + ":" + header_info[0].port;
function initial(){
var is_logined = ["1"][0];
var html_code = '';
var url_flag = "";
var html_code_notlogin = "<ul><li>ネットワーク管理者にご相談ください。</li></ul>";
var showtext = function(obj, str){if(obj)obj.innerHTML=str;}
if(odm_support){
$('.model_img').attr('class', 'mode_img_COD');
}
if(casenum == 1){
$("#page_title").html("イーサネット ケーブルが接続されていません。");
html_code += "<ul>";
html_code += "<li>ケーブルが TUF GAMING AX4200 WAN ポートとモデムに接続されていることご確認ください。</li>";
html_code += "<li><a style='color:#FFF' href='/Advanced_OperationMode_Content.asp'>動作モード</a>を変更する必要があるかをご確認ください。</li>";
html_code += "</ul>";
$("#wanLink").click(function(){
detect_general();
});
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else if(casenum == 2){
html_code += "<ul>";
html_code += "<li>";
if(wansbstate == 2 || wanauxstate == 3){ //Authentication Failed
$("#page_title").html("PPPoE 認証の失敗");
html_code += "<div>PPPoE アカウントまたはパスワードが正しくありません。<a style='color:#FFF' href='/Advanced_WAN_Content.asp'>確認</a>してください。</div>";
$("#wanLink").click(function(){
});
}
else if(wansbstate == 1){ //No Response
}
else if(wansbstate == 10){ //Terminal due to lack of activity
}
else{ //Connecting
$("#animation_field").show();
detect_ppp_connect();
$("#page_title").html("インターネットに再接続中です。");
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggest_title").hide();
$("#suggestion").hide();
$("#case_content").hide();
$("#back_btn").show();
$("#wanLink").click(function(){
history.go(-1);
});
$("#wanLink").html("前のページ");
}
html_code += "</li>";
html_code += "</ul>";
$("#wanLink").hide();
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else if(casenum == 3){
$("#page_title").html("インターネットに接続できません。");
html_code += "<ul>";
html_code += "<li><a style='color:#FFF' href='/Advanced_WAN_Content.asp'>接続設定</a>が正しいことを確認してください。</li>";
html_code += "<li>ISP(Internet Service Provider) に連絡し、DHCP のエラーの原因をご確認ください。</li>";
html_code += "</ul>";
$("#wanLink").click(function(){
detect_general();
});
$("#wanLink").html("WAN のタイプを変更する");
$("#wanLink").hide();
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else if(casenum == 4){
showtext($("#failReason1")[0], "インターネットへの接続に失敗しました。ルーターの IP アドレスがゲートウェイの IP アドレスと同じです。");
html_code += "<ul>";
html_code += "<li>ルーターの IP アドレスをゲートウェイの IP アドレスとは異なるアドレスに設定してください。</li>";
html_code += "</ul>";
$("#wanLink").click(function(){
detect_general();
});
}
else if(casenum == 5){
if(wanstate == 5){
$("#page_title").html("WAN接続が無効になりました。");
}
else{
$("#page_title").html("USBモデムが接続されていません。");
}
html_code += '<ul>';
if(wanstate == 5){
html_code += "<li><a style='color:#FFF' href='/'>WAN 接続</a>を有効にする</li>";
}
else{
html_code += "<li>USBモデムの電源が入っていることをご確認ください。</li>";
html_code += "<li><a style='color:#FFF' href='/Advanced_Modem_Content.asp'>USB モデム設定</a>を変更してください。</li>";
}
html_code += '</ul>';
if(wanstate == 5){
$("#wanLink").click(function(){
manually_start_wan_Link();
});
}else{
$("#wanLink").click(function(){
detect_general();
});
}
$("#wanLink").hide();
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else if(casenum.search("6") !== -1){
$("#page_title").html("IP アドレスの競合が検出されました。");
html_code += "<ul>";
html_code += "<li>次の IP アドレスを使用する場合は、[次へ]をクリックしてください。";
html_code += "<span style='font-weight:bolder'>"+ new_lan_ip +"</span></li>";
html_code += "<li>すべての関連機能で新しいIPアドレスを使用していることをご確認ください（例：ポートフォワーディング、DMZなど）。</li>";
html_code += "</ul>";
$("#wanLink").html("次へ");
$("#wanLink").click(function(){
change_lan_subnet();
});
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else if(casenum == 8){
$("#page_title").html("メインのアクセスポイントに接続できません。");
if(!is_logined){
html_code = html_code_notlogin;
$("#wanLink").hide();
}
else{
html_code += "<ul>";
html_code += "<li>メインのアクセスポイントがインターネットに接続できることをご確認ください。</li>";
html_code += "<li><a style='color:#FFF' href='/QIS_wizard.htm?flag=manual'>接続設定を変更します</a>。</li>";
html_code += "</ul>";
if(sw_mode == "2"){
if(wlc_express == '1')
url_flag += "sitesurvey_exp2";
else if(wlc_express == '2')
url_flag += "sitesurvey_exp5";
else
url_flag += "sitesurvey_rep";
}
else
url_flag += "sitesurvey_mb";
$("#wanLink").click(function(){
top.location.href = "/QIS_wizard.htm?flag=" + url_flag;
});
}
$("#wanLink").hide();
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else if(casenum == 9) {
$("#page_title").html("メインのアクセスポイントに接続できません。");
html_code += "<ul>";
html_code += "<li>AiMeshルーターの電源が入っていることをご確認ください。</li>";
html_code += "<li>AiMeshルーターを再起動してやり直してください。</li>";
html_code += "</ul>";
$("#wanLink").hide();
$("#reason_title").hide();
$("#reason_field").hide();
$("#suggestion").hide();
}
else{
parent.location = '/';
}
$("#case_content")[0].innerHTML = html_code;
if(casenum == "6_1"){
change_lan_subnet();
}
var windowHeight = (function(){
if(window.innerHeight)
return window.innerHeight;
else if(document.body && document.body.clientHeight)
return document.body.clientHeight;
else if(document.documentElement && document.documentElement.clientHeight)
return document.documentElement.clientHeight;
else
return 800;
})();
document.getElementById("loginTable").style.display = "";
}
function pppoeLink(){
top.location.href = "/QIS_wizard.htm?flag=pppoe";
}
function detectLink(){
top.location.href = "/QIS_wizard.htm?flag=detect";
}
function manually_start_wan_Link(){
top.location.href = '/index.asp'+"?flag=Internet";
}
function change_lan_subnet(){
top.location.href = "/updateSubnet.htm";
}
function detect_router(){
$.ajax({
url: location_org.replace(header_info[0].host, new_lan_ip) + "/repage.json",
dataType: "script",
timeout: 5000,
success: function(){
top.location.href = location_org.replace(header_info[0].host, new_lan_ip)
+ "/QIS_wizard.htm?flag="
+ (function(){return (('1' === '0')?"welcome":"detect")})();
},
error: function(){
setTimeout(detect_router, 1000);
setTimeout(function(){
$("#case_content ul").html("<li>IP アドレスが更新しています。更新作業に2分以上かかる場合は、次の手順で IP を手動で更新してください。(1) ネットワークケーブルを抜く。 (2) 10秒ほど待機する。 (3) ケーブルを再度接続し新しい IP アドレスを取得する。</li>");
}, 3000);
}
});
}
function detect_general(){
if(wans_flag){ //Dual WAN
if(wans_dualwan_orig.split(" ")[0].toUpperCase() == "USB"){
if(gobi_support)
top.location.href = '/Advanced_MobileBroadband_Content.asp';
else
top.location.href = '/Advanced_Modem_Content.asp';
}else if(dsl_support){
if(wans_dualwan_orig.split(" ")[0].toUpperCase() == "WAN" || wans_dualwan_orig.split(" ")[0].toUpperCase() == "LAN")
top.location.href = '/Advanced_WAN_Content.asp';
else
top.location.href = '/Advanced_DSL_Content.asp';
}
else
top.location.href = '/Advanced_WAN_Content.asp';
}
else{ //Single WAN
if(dsl_support)
top.location.href = '/Advanced_DSL_Content.asp';
else if(wans_dualwan_orig.split(" ")[0].toUpperCase() == "USB")
top.location.href = '/Advanced_MobileBroadband_Content.asp';
else if(sw_mode == 3)
top.location.href = '/';
else
top.location.href = '/Advanced_WAN_Content.asp';
}
}
function detect_ppp_connect(){
$.ajax({
url: '/WAN_info.asp',
dataType: 'script',
error: function(xhr){
setTimeout(detect_ppp_connect, 1000);
},
success: function(response){
if( wanstate == "2" && wansbstate == "0" && wanauxstate == "0"){
top.location.href = '/';
}
else{
setTimeout(detect_ppp_connect, 1000);
}
}
});
}
</script>
</head>
<body class="wrapper" onload="initial();">
<div id="loginTable" class="div_table main_field_gap" style="display:none">
<div class="title_name">
<div class="div_td img_gap">
<div class="login_img"></div>
</div>
<div id="page_title" class="div_td title_text">表示したい Web ページを読み込めませんでした。</div>
</div>
<div class="prod_madelName">TUF GAMING AX4200</div>
<div id="reason_title" class="p1 title_gap">接続失敗の原因</div>
<div id="reason_field">
<div class="p1 title_gap"></div>
<div class="nologin">
<div id="failReason1"></div>
</div>
</div>
<div id="suggest_title" class="p1 title_gap">対応方法：</div>
<div>
<div class="p1 title_gap"></div>
<div class="nologin">
<div id="animation_field" style="display:none">
<div style="display:table">
<div style="display:table-row">
<div style="display:table-cell">
<div class="model_img"></div>
</div>
<div style="display:table-cell;width:300px;vertical-align:middle;position:relative">
<div style="width:200px;height:3px;background:#279FD9;margin-left:30px;"></div>
<div class="connect" style="width:12px;height:12px;border-radius:100px;position:absolute;background:#FFF;top:64px;left:30px;"></div>
</div>
<div style="display:table-cell">
<div style="width:110px;height:130px;background:url('images/Internet.png') no-repeat;"></div>
</div>
</div>
</div>
</div>
<div id="case_content"></div>
<div id="suggestion">
<ul>
<li>
<span>問題が解決しない場合は、手動で接続設定を変更してください。</span>
</li>
</ul>
</div>
</div>
</div>
<div>
<div id="wanLink" class='button'>設定</div>
<div id="submitBtn" class='button button_background' style="display:none"></div>
</div>
</body>
</html>

