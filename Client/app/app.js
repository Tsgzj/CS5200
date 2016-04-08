'use strict';

var server;
server = "http://private-1db78-sunwenxiang.apiary-mock.com"
// server = "http://127.0.0.1:5000"

// Declare app level module which depends on views, and components
var myApp = angular.module('myApp', [
  'ui.router',
  'ui.bootstrap',
  'ngCookies'
]).
config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("front")
  $stateProvider
      .state('front', {
          url: "/front",
          templateUrl: "static/frontPage.html"
      })
      .state('login', {
        url: "/login",
        templateUrl: "static/login.html"
      })
      .state('electronics', {
        url: "/category",
        templateUrl: "static/category.html",
        controller: function($scope, $http) {
            $http({
                method: "GET",
                url: server + "/category?category=electronics"
            }).then(function (response) {
                $scope.items = response.data;
            }, function(response) {
                window.alert("Something wrong happened, please try again.")
            });
        }
      })
      .state('fashion', {
          url: "/category",
          templateUrl: "static/category.html",
          controller: function ($scope, $http) {
              $http({
                  method: "GET",
                  url: server + "/category?category=fashion"
              }).then(function (response) {
                  $scope.items = response.data;
              }, function(response) {
                  window.alert("Something wrong happened, please try again.")
              });
          }
      })
      .state('home', {
        url: "/category",
        templateUrl: "static/category.html",
        controller: function($scope, $http) {
            $http({
                method : "GET",
                url : server + "/category?category=home"
            }).then(function(response) {
                $scope.items = response.data;
            }, function(response) {
                window.alert("Something wrong happened, please try again.")
            });
        }
      })
      .state('profile', {
          url: "/profile",
          params: {
              userid: null
          },
          templateUrl: "static/profile.html",
          controller: function($scope, $http, $stateParams) {
              $http({
                  method: "GET",
                  url: server + "/user?userid=" + $stateParams.userid
              }).then(function (response) {
                  $scope.profile = response.data;
              }, function(response) {
                  window.alert("Please log in first.")
              });
          }
      })
      .state('inventory', {
        url: "/inventory",
        templateUrl: "static/inventory.html",
        params: {
            term: null
        },
        controller: function($scope, $http, $stateParams) {
            $http({
                method: "GET",
                url: server + "/inventory?title=" + $stateParams.term
            }).then(function (response) {
                $scope.items = response.data;
            }, function(response) {
                window.alert("Something wrong happened, please try again.")
            });
        }
      })
      .state('addpayment', {
          url: "/addpayment",
          templateUrl: "static/addPayment.html"
      })
      .state('detailpayment', {
          url: "/payment",
          templateUrl: "static/detailPayment.html",
          controller: function($scope, $http, $cookies) {
              $http({
                  method: "GET",
                  url: server + "/user/payment?UserId=" + $cookies.get("uid")
              }).then(function (response) {
                  $scope.data = response.data;
              }, function(response) {
                  window.alert("Please log in first.")
              });
          }
      })
      .state('editpayment', {
          url: "/editpayment",
          templateUrl: "static/editPayment.html",
          params: {
              cardNumber: null
          },
          controller: function($scope, $stateParams) {
              $scope.cardNumber = $stateParams.cardNumber
          }
      })
      .state('order', {
          url: "/order",
          templateUrl: "static/order.html"
      })
});

myApp.controller('BannerCtrl', ['$scope', '$log', '$state', '$cookies', '$http', function($scope, $log, $state, $cookies, $http) {
    $scope.search = function() {
        $state.go('inventory', {term: $scope.term});
    }
    $scope.checkLogin = function() {
        var userid = $cookies.get("uid");
        if(userid) {
            $scope.uid = userid;
            return false;
        }
        else
            return true;
    }
    $scope.foo = function() {
        $cookies.put("uid", "123");
    }
    $scope.logout = function() {
        $http.delete(server + "/session?uid=" + $cookies.get("uid")
        ).success(
            $cookies.remove("uid"),
            $state.go('front')
        ).error(
            window.alert("Something wrong happend")
        )
    }
    $scope.login = function() {
        $http({
            method: "GET",
            url: server + "/session?username=" + $scope.userName + "&password=" + $scope.passWord
        }).then(function(response) {
            $cookies.put("uid", response.data.UserId),
            $state.go('profile', {userid: $cookies.get("uid")})
        }, function(response) {
            window.alert("Cannot verify the username/password pair")
        })
    }
}]);

myApp.controller('ProfileCtrl', ['$scope', '$http', '$state', '$cookies', function($scope, $http, $state, $cookies) {
    $scope.typeoptions = ["Visa", "Master", "AmericanExpress"];
    $scope.cardType = $scope.typeoptions[0];
    $scope.addNewPayment = function() {
        var requestData = {};
        if($scope.preChk()) {
            requestData["UserId"] = $cookies.get("uid"),
            requestData["CardNumber"] = $scope.cardNumber,
            requestData["Address"] = $scope.cardAddress,
            requestData["ExpirationDate"] = $scope.expirationDate,
            requestData["Type"] = $scope.cardType,
            $http.post(server + "/user/payment", requestData).success(
                $state.go('profile', {userid: $cookies.get("uid")})
            ).error(
                window.alert("Failed to update payment.")
            )
        }
    }
    $scope.editPayment = function() {
        var requestData = {};
        console.log($scope.cardNumber);
        if($scope.preChk()) {
            requestData["UserId"] = $cookies.get("uid"),
            requestData["CardNumber"] = $scope.cardNumber,
            requestData["Address"] = $scope.cardAddress,
            requestData["ExpirationDate"] = $scope.expirationDate,
            requestData["Type"] = $scope.cardType,
            $http.post(server + "/user/payment/" + $scope.cardNumber, requestData).success(
                $state.go('profile', {userid: $cookies.get("uid")})
            ).error(
                window.alert("Failed to update payment.")
            )
        }
    }
    $scope.preChk = function() {
        if($scope.cardNumber == null || $scope.cardAddress == null || $scope.expirationDate == null || $scope.cardType == null){
            window.alert("Please fill all the columns");
            return false;
        }
        if(!$scope.checkCard($scope.cardNumber)){
            window.alert("Invalid Card Number");
            return false;
        }
        if(!$scope.checkDateFormat($scope.expirationDate)){
            window.alert("Invalid ExpirationDate");
            return false;
        }
        return true;
    }
    $scope.checkCard = function(cardNumber){
        if (cardNumber.length != 16) {
            return false;
        }
        if(isNaN(cardNumber)) {
            return false;
        }
        if (!$scope.checkCardNumber(cardNumber)) {
            return false;
        }
        return true;
    }
    $scope.checkCardNumber = function(value){
        // get from https://gist.github.com/DiegoSalazar/4075533
        if (/[^0-9-\s]+/.test(value)) return false;

        // The Luhn Algorithm. It's so pretty.
        var nCheck = 0, nDigit = 0, bEven = false;
        value = value.replace(/\D/g, "");

        for (var n = value.length - 1; n >= 0; n--) {
            var cDigit = value.charAt(n),
                nDigit = parseInt(cDigit, 10);

            if (bEven) {
                if ((nDigit *= 2) > 9) nDigit -= 9;
            }

            nCheck += nDigit;
            bEven = !bEven;
        }

        return (nCheck % 10) == 0;
    }
    $scope.checkDateFormat = function(dateString){
        // get from http://stackoverflow.com/questions/6177975/how-to-validate-date-with-format-mm-dd-yyyy-in-javascript
        if(!/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(dateString))
            return false;

        // Parse the date parts to integers
        var parts = dateString.split("/");
        var day = parseInt(parts[1], 10);
        var month = parseInt(parts[0], 10);
        var year = parseInt(parts[2], 10);

        // Check the ranges of month and year
        if(year < 1000 || year > 3000 || month == 0 || month > 12)
            return false;

        var monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

        // Adjust for leap years
        if(year % 400 == 0 || (year % 100 != 0 && year % 4 == 0))
            monthLength[1] = 29;

        // Check the range of the day
        return day > 0 && day <= monthLength[month - 1];
    }
}])
