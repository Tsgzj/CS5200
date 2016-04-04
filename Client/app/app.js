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
        templateUrl: "login.html"
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
});

myApp.controller('BannerCtrl', ['$scope', '$log', '$state', function($scope, $log, $state) {
    $scope.search = function() {
        $state.go('inventory', {term: $scope.term});
    }
}]);
