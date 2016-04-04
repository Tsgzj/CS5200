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
        templateUrl: "static/category.html",
        controller: function($scope, $http) {
            $http({
                method: "GET",
                url: "http://127.0.0.1:5000/category?category=electronics"
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
                  url: "http://127.0.0.1:5000/category?category=fashion"
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
                url : "http://127.0.0.1:5000/category?category=home"
            }).then(function(response) {
                $scope.items = response.data;
            });
        }
      })
      .state('inventory', {
        url: "/inventory",
        templateUrl: "static/inventory.html",
        controller: function($scope){
          $scope.items = [{
              "InventoryId": 2,
              "Title": "Mouse",
              "Description": "",
              "Price": 68,
              "Discount": 1,
              "Category": "Electronics",
              "Available": 15
          },
          {
              "InventoryId": 1,
              "Title": "Keyboard",
              "Description": "",
              "Price": 100,
              "Discount": 0.95,
              "Category": "Electronics",
              "Available": 5
          }];
        }
      })
});
