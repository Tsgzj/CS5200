'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
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
        templateUrl: "category.html"
      })
      .state('fashion', {
        url: "/category",
        templateUrl: "category.html"
      })
      .state('home', {
        url: "/category",
        templateUrl: "category.html"
      })
      .state('inventory', {
        url: "/inventory",
        templateUrl: "inventory.html",
        controller: function($scope){
          $scope.items = ["A", "List", "Of", "Items"];
        }
      })
});
