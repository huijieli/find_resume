// Copyright 2009 FriendFeed
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.


$("div").click(function(){
	$(this).css("background-color","gray");
	
	
});
var passport=0
$(document).ready(function() {
	
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};
    
    passport=prompt("Enter your passport!");
    $("h1").text(passport+"的最新通知数:");
    updater.poll();
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function() {
        var args = {"_xsrf": getCookie("_xsrf"),"passport":passport};
        $.ajax({url: "/push", type: "POST", dataType: "text",
                data: $.param(args), success: updater.onSuccess,
                error: updater.onError});
    },

    onSuccess: function(response) {
    	response.cursor
    	$("p").text(eval("(" + response + ")").messages);
    	$("p").css({
    		  "color":"red",
    		  "font-family":"Arial",
    		  "font-size":"100px",
    		  "padding":"5px"
    		  });
    	
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },


};
