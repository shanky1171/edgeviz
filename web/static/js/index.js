document.addEventListener('DOMContentLoaded', function() {

  document.querySelector('#sub-menu').style.visibility='hidden';

  document.querySelector('#mDefine').onclick = function(){
    document.querySelector('#ldefine').style.color='red';

    document.querySelector('#mConnect').style.visibility='hidden';
    document.querySelector('#mMonitor').style.visibility='hidden';
    document.querySelector('#mManage').style.visibility='hidden';
    document.querySelector('#mAnalyze').style.visibility='hidden';
    document.querySelector('#mMonetize').style.visibility='hidden';

    document.querySelector('#sub-menu').style.visibility='visible';

    /*var divDefine = document.createElement('div');
    divDefine.setAttribute('class', 'row');
    divDefine.style.marginTop = "30px";
    divDefine.style.marginLeft = "100px";

    var divDefineMenu1 = document.createElement('div');
    divDefineMenu1.setAttribute('class', 'main-menu-col');
    divDefine.appendChild(divDefineMenu1);
    var imgDefineMenu1 = document.createElement('img');
    imgDefineMenu1.style.height = "100px";
    imgDefineMenu1.style.width = "100px";
    imgDefineMenu1.src = 'static/images/Define/Enterprise.png';
    divDefineMenu1.appendChild(imgDefineMenu1);
    var lblDefineMenu1 = document.createElement('h6');
    lblDefineMenu1.style.textAlign ="center";
    lblDefineMenu1.innerHTML="Enterprise";
    divDefineMenu1.appendChild(lblDefineMenu1);

    var divDefineMenu2 = document.createElement('div');
    divDefineMenu2.setAttribute('class', 'main-menu-col');
    divDefine.appendChild(divDefineMenu2);
    var imgDefineMenu2 = document.createElement('img');
    imgDefineMenu2.style.height = "100px";
    imgDefineMenu2.style.width = "100px";
    imgDefineMenu2.src = 'static/images/Define/Site.jpeg';
    divDefineMenu2.appendChild(imgDefineMenu2);
    var lblDefineMenu2 = document.createElement('h6');
    lblDefineMenu2.style.textAlign ="center";
    lblDefineMenu2.innerHTML="Site";
    divDefineMenu2.appendChild(lblDefineMenu2);

    var divDefineMenu3 = document.createElement('div');
    divDefineMenu3.setAttribute('class', 'main-menu-col');
    divDefine.appendChild(divDefineMenu3);
    var imgDefineMenu3 = document.createElement('img');
    imgDefineMenu3.style.height = "100px";
    imgDefineMenu3.style.width = "100px";
    imgDefineMenu3.src = 'static/images/Define/DeviceType.jpeg';
    divDefineMenu3.appendChild(imgDefineMenu3);
    var lblDefineMenu3 = document.createElement('h6');
    lblDefineMenu3.style.textAlign ="center";
    lblDefineMenu3.innerHTML="Device Type";
    divDefineMenu3.appendChild(lblDefineMenu3);

    var divDefineMenu4 = document.createElement('div');
    divDefineMenu4.setAttribute('class', 'main-menu-col');
    divDefine.appendChild(divDefineMenu4);
    var imgDefineMenu4 = document.createElement('img');
    imgDefineMenu4.style.height = "100px";
    imgDefineMenu4.style.width = "100px";
    imgDefineMenu4.src = 'static/images/Define/Device.png';
    divDefineMenu4.appendChild(imgDefineMenu4);
    var lblDefineMenu4 = document.createElement('h6');
    lblDefineMenu4.style.textAlign ="center";
    lblDefineMenu4.innerHTML="Device";
    divDefineMenu4.appendChild(lblDefineMenu4);

    document.body.appendChild(divDefine);
    */

  };
});


function OnConnectClick()
{
 alert("Someone clicked on Connect");
}

function OnMonitorClick()
{
  alert("Someone clicked on Monitor");
}

function OnManageClick()
{
  alert("Someone clicked on Manage");
}

function OnAnalyzeClick()
{
  alert("Someone clicked on Analyze");
}

function OnMonetizeClick()
{
  alert("Someone clicked on Monetize");
}
