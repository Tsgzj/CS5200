'use strict';

var server;
server = "http://private-1db78-sunwenxiang.apiary-mock.com"
// server = "http://127.0.0.1"

// Declare app level module which depends on views, and components
var myApp = angular.module('myApp', [
  'ui.router',
  'ui.bootstrap',
  'ngCookies'
]).
config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise("/")
  $stateProvider
      .state('login', {
        url: "/login",
        templateUrl: "static/category.html"
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
              })
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
            });
        }
      })
      .state('addpayment', {
          url: "/addpayment",
          templateUrl: "static/payment.html"
      })
});

myApp.controller('BannerCtrl', ['$scope', '$log', '$state', '$cookies', function($scope, $log, $state, $cookies) {
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
    $scope.bar = function() {
        $cookies.remove("uid");
        console.log("Remove cookies");
    }
}]);

myApp.controller('ProfileCtrl', ['$scope', '$http', '$state', '$cookies', function($scope, $http, $state, $cookies) {
    $scope.addNewPayment = function() {
        var requestData = {};
        requestData["UserId"]="test",
        requestData["CardNumber"]="123456789877",
        requestData["Address"]="361 Huntington Ave",
        requestData["ExpirationDate"]="04/11/2016",
        requestData["Type"]="Visa"
        $http.post(server + "/user/payment", requestData).
        success(
            $state.go('profile')
        ).
        error(
            window.alert("Failed to update payment.")
        )
    }
}])
