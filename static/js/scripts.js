

var chicagoApp = angular.module('chicagoApp', []);

chicagoApp.controller('ChicagoCtrl', function ($scope, $log, $compile, $window, $interval, $http) {
    $scope.todoHasChanged = false;
    $scope.todo = "";
    
    angular.element(document).ready(function () {
    	init();
    });
    
    String.prototype.replaceAll = function(s,r){return this.split(s).join(r)}
    
    function init() {
    	$http.get('/chicago/get').
		  then(function(response) {
		      var todo = response.data;
	          todo = todo.replaceAll("%26", "&");
			  $scope.todo = todo;
		  }, function(errorResponse) {
			  alert(errorResponse);
		  });
    };
    
    $interval(saveTodos, 1000);
    
    function saveTodos() {
    	if ($scope.todoHasChanged) {
    	    var todo = $scope.todo;
    	    todo = todo.replaceAll("&", "%26");
    		$http.get('/chicago/put?message=' + todo).
    		  then(function(response) {
    			  console.log("Saved " + response);
    		  }, function(errorResponse) {
    			  alert(errorResponse);
    		  });
    		
    		console.log(todo);
        	$scope.todoHasChanged = false;
    	}
    }
    
    $scope.newValue = function() {
    	$scope.todoHasChanged = true;
    }
});







(function (e) {
  e.fn.countdown = function (t, n) {
  function i() {
    eventDate = Date.parse(r.date) / 1e3;
    currentDate = Math.floor(e.now() / 1e3);
    if (eventDate <= currentDate) {
      n.call(this);
      clearInterval(interval)
    }
    seconds = eventDate - currentDate;
    days = Math.floor(seconds / 86400);
    seconds -= days * 60 * 60 * 24;
    hours = Math.floor(seconds / 3600);
    seconds -= hours * 60 * 60;
    minutes = Math.floor(seconds / 60);
    seconds -= minutes * 60;
    days == 1 ? thisEl.find(".timeRefDays").text("day") : thisEl.find(".timeRefDays").text("days");
    hours == 1 ? thisEl.find(".timeRefHours").text("hour") : thisEl.find(".timeRefHours").text("hours");
    minutes == 1 ? thisEl.find(".timeRefMinutes").text("minute") : thisEl.find(".timeRefMinutes").text("minutes");
    seconds == 1 ? thisEl.find(".timeRefSeconds").text("second") : thisEl.find(".timeRefSeconds").text("seconds");
    if (r["format"] == "on") {
      days = String(days).length >= 2 ? days : "0" + days;
      hours = String(hours).length >= 2 ? hours : "0" + hours;
      minutes = String(minutes).length >= 2 ? minutes : "0" + minutes;
      seconds = String(seconds).length >= 2 ? seconds : "0" + seconds
    }
    if (!isNaN(eventDate)) {
      thisEl.find(".days").text(days);
//      thisEl.find(".hours").text(hours);
//      thisEl.find(".minutes").text(minutes);
//      thisEl.find(".seconds").text(seconds)
    } else {
      alert("Invalid date. Example: 30 Tuesday 2013 15:50:00");
      clearInterval(interval)
    }
  }
  var thisEl = e(this);
  var r = {
    date: null,
    format: null
  };
  t && e.extend(r, t);
  i();
  interval = setInterval(i, 1e3)
  }
  })(jQuery);
  $(document).ready(function () {
  function e() {
    var e = new Date;
    e.setDate(e.getDate() + 60);
    dd = e.getDate();
    mm = e.getMonth() + 1;
    y = e.getFullYear();
    futureFormattedDate = mm + "/" + dd + "/" + y;
    return futureFormattedDate
  }
  $("#countdown").countdown({
    date: "28 October 2015 00:00:00", // Change this to your desired date to countdown to
    format: "on"
  });
});