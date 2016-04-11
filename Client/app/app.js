'use strict';

var server;
//server = "http://private-1db78-sunwenxiang.apiary-mock.com"
server = "http://127.0.0.1:5000"

// Declare app level module which depends on views, and components
var myApp;
myApp = angular.module('myApp', [
    'ui.router',
    'ui.bootstrap',
    'ngCookies'
]).config(function ($stateProvider, $urlRouterProvider) {
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
            controller: function ($scope, $http) {
                $http({
                    method: "GET",
                    url: server + "/category?category=electronics"
                }).then(function (response) {
                    $scope.items = response.data;
                }, function (response) {
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
                }, function (response) {
                    window.alert("Something wrong happened, please try again.")
                });
            }
        })
        .state('home', {
            url: "/category",
            templateUrl: "static/category.html",
            controller: function ($scope, $http) {
                $http({
                    method: "GET",
                    url: server + "/category?category=home"
                }).then(function (response) {
                    $scope.items = response.data;
                }, function (response) {
                    window.alert("Something wrong happened, please try again.")
                });
            }
        })
        .state('profile', {
            url: "/profile",
            templateUrl: "static/profile.html",
            controller: function ($scope, $http, $cookies) {
                $http({
                    method: "GET",
                    url: server + "/user?UserId=" + $cookies.get("uid")
                }).then(function (response) {
                    $scope.profile = response.data;
                }, function (response) {
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
            controller: function ($scope, $http, $stateParams) {
                $http({
                    method: "GET",
                    url: server + "/inventory?title=" + $stateParams.term
                }).then(function (response) {
                    $scope.items = response.data;
                }, function (response) {
                    window.alert("Something wrong happened, please try again.")
                });
            }
        })
        .state('detail', {
            url: "/inventory/detail",
            templateUrl: "static/inventoryDetail.html",
            params: {
                data: {}
            },
            controller: function ($scope, $stateParams) {
                //console.log($stateParams.data);
                $scope.item = $stateParams.data;
            }
        })
        .state('addpayment', {
            url: "/addpayment",
            templateUrl: "static/addPayment.html"
        })
        .state('detailpayment', {
            url: "/payment",
            templateUrl: "static/detailPayment.html",
            controller: function ($scope, $http, $cookies) {
                $http({
                    method: "GET",
                    url: server + "/user/payment?UserId=" + $cookies.get("uid")
                }).then(function (response) {
                    $scope.data = response.data;
                }, function (response) {
                    window.alert("Please log in first.")
                });
            }
        })
        .state('editpayment', {
            url: "/editpayment",
            templateUrl: "static/editPayment.html",
            params: {
                cardNumber: null,
                cardId: null
            },
            controller: function ($scope, $stateParams) {
                console.log("Here");
                $scope.cardNumber = $stateParams.cardNumber;
                $scope.cardId = $stateParams.cardId;
                console.log($scope.cardId)
            }
        })
        .state('order', {
            url: "/order",
            templateUrl: "static/order.html",
            params: {
                orderid: null
            },
            controller: function ($scope, $http, $cookies, $stateParams) {
                $http({
                    method: "GET",
                    url: server + "/order?UserId=" + $cookies.get("uid") + "&CartOrderId=" + $stateParams.orderid
                }).then(function (response) {
                    $scope.data = response.data;
                    var sum = 0;
                    for(var i=0; i<$scope.data.Item.length; i++) {
                        if (i in $scope.data.Item) {
                            var s = $scope.data.Item[i];
                            sum += s.Price * s.Discount * s.Quantity;
                        }
                    }
                    $scope.total = sum;
                }, function (response) {
                    window.alert("Please log in first.")
                });
            }
        })
        .state('orderconfirm', {
            url: "/orderConfirm",
            templateUrl: "static/orderConfirmation.html",
            params: {
                confirm: null
            },
            controller: function ($scope, $stateParams) {
                $scope.confirm = $stateParams.confirm;
            }
        })
        .state('shoppingcart', {
      		url:"/shoppingcart",
      		templateUrl: "static/shoppingCart.html",
      		controller : function($scope,$http,$cookies){
      			$http({
      				method : "GET",
      				url: server + "/shoppingcart?UserId=" + $cookies.get("uid")
      			}).then(function(response){
                    $cookies.put("shopcartid", response.data.ShoppingCartId),
                    $scope.json=response.data;
                    var sum = 0;
                    if($scope.json.Item.length>0) {
                        for (var i = 0; i < $scope.json.Item.length; i++) {
                            if (i in $scope.json.Item) {
                                var s = $scope.json.Item[i];
                                sum += s.Price * s.Discount * s.Quantity;
                            }
                        }
                        $scope.total = parseFloat(sum).toFixed(2);
                        $scope.cancheckout = true;
                    }
                    else {
                        $scope.message = "You have nothing in your cart";
                        $scope.cancheckout = false
                    }
      			}, function(response){
      				window.alert("Please Login first.")
      			});
      		}
        })
        .state('checkout', {
            url:"/checkout",
            templateUrl: "static/checkout.html",
            params: {
                item: {},
                total: null,
                shopcartid: null,
            },
            controller: function($scope, $stateParams) {
                $scope.items = $stateParams.item;
                $scope.total = $stateParams.total;
                $scope.shopcCartId = $stateParams.shopcartid;
                console.log($stateParams.shopCartId)
            }
        })
        .state('addInventory',{
            url:"/addInventory",
            templateUrl:"static/addInventory.html",
            controller: function($scope,$http){
                $http({
                    method: "POST",
                    url: server + "/inventory"
                }).then(function(response){
                    $scope.data=response.data;
                })

            }

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
            $cookies.remove('uid'),
            $cookies.remove('shopcartid'),
            $state.go('front')
        ).error(
            window.alert("Something wrong happend")
        )
    }
    $scope.logIn = function() {
        console.log("Clicked");
        $http({
            method: "GET",
            url: server + "/session?username=" + $scope.userName + "&password=" + $scope.passWord
        }).then(function(response) {
            console.log(response.data);
            $cookies.put("uid", response.data.UserId),
            $state.go('profile')
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
                $state.go('profile')
            ).error(
                window.alert("Failed to update payment.")
            )
        }
    }
    $scope.editPayment = function() {
        var requestData = {};
        //console.log($scope.cardNumber);
        if($scope.preChk()) {
            requestData["UserId"] = Number($cookies.get("uid")),
            requestData["CardNumber"] = $scope.cardNumber,
            requestData["Address"] = $scope.cardAddress,
            requestData["ExpirationDate"] = $scope.expirationDate,
            requestData["Type"] = $scope.cardType,
            $http.post(server + "/user/updatepayment?cardId=" + $scope.cardId, requestData).success(
                $state.go('profile')
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

myApp.controller('ShoppingCartCtrl', ['$scope', '$log', '$state', '$cookies', '$http', function($scope, $log, $state, $cookies, $http) {
    $scope.addToCart = function () {
        var requestData = {};
        if($scope.preChk($scope.item.Available, $scope.number)) {
            requestData["Quantity"] = $scope.number;
            requestData["InventoryId"] = $scope.item.InventoryId;
            requestData["UserId"] = Number($cookies.get("uid"));
            requestData["ShoppingCartId"] = $cookies.get("shopcartid")
            $http.post(server + "/shoppingcart", requestData).success(
                $state.go('shoppingcart')
            ).error(
                window.alert("Failed to update payment.")
            )
        }
        else {
            window.alert("Cannot fullfill your request now")
        }
    }
    $scope.deleteCart = function (id) {
        $http.delete(server + "/shoppingcart?userid=" + $cookies.get('uid') + "&inventoryid=" + id + "&shoppingcartid=" + $cookies.get("shopcartid"))
            .success(
                $state.go('shoppingcart')
            ).error(
            window.alert("Failed to delete item.")
        )
    }
    $scope.preChk = function(aval, num) {
        if (isNaN(num)){
            return false;
        }
        return num<=aval;
    }
}])

//myApp.controller('CheckoutCtrl', ['scope', '$state', '$cookies', '$http', function($scope, $state, $cookies, $http) {
myApp.controller('CheckoutCtrl', ['$scope', '$log', '$state', '$cookies', '$http', function($scope, $log, $state, $cookies, $http) {
        $http({
            method: "GET",
            url: server + "/user?UserId=" + $cookies.get("uid")
        }).then(function(response) {
            $scope.payment = response.data.Payment;
            $scope.cards = $scope.payment[0];
        }, function() {
            window.alert("Failed to get payment info")
        })
        $http({
            method: "GET",
            url: server + "/user?UserId=" + $cookies.get("uid")
        }).then(function(response) {
            $scope.shippingAddresses = response.data.ShippingAddress;
            $scope.shipping = $scope.shippingAddresses[0];
            console.log($scope.shipping);
        }, function() {
            window.alert("Failed to get payment info")
        })
        $http({
            method: "GET",
            url: server + "/user?UserId=" + $cookies.get("uid")
        }).then(function(response) {
            $scope.billingAddresses = response.data.BillingAddress;
            $scope.billing = $scope.billingAddresses[0];
        }, function() {
            window.alert("Failed to get payment info")
        })
        $scope.checkout = function() {
            //console.log("Check Out");
            var requestData = {};
            requestData["UserId"] = Number($cookies.get("uid"));
            requestData["CardId"] = $scope.cards.CardId;
            requestData["CartId"] = Number($cookies.get("shopcartid"));
            requestData["ShippingAddressId"] = $scope.shipping.AddressId;
            requestData["BillingAddressId"] = $scope.billing.AddressId;
            //console.log(requestData);
            $http({
                method: "POST",
                url: server + "/order",
                data: requestData
            }).then(function(response) {
                console.log(response.data.CartOrderId);
                $cookies.remove("shopcartid");
                $state.go('orderconfirm', {confirm: response.data.CartOrderId});
            }, function() {
                window.alert("Failed to update payment.")
            })
        }
}])
