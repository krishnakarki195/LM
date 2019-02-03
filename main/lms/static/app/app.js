var dependencies, LmApp;

dependencies = [ 'ui.bootstrap' 'ui.router', 'LmApp.common', 'LmApp.controllers',
    'LmApp.services', 'LmApp.factories', 'LmApp.models','LmApp.directives',
    'LmApp.filters',];

LmApp = angular.module('LmApp', dependencies);
LmApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('home', {
            url: '/log',
            templateUrl: '/home/components/components.html'
        }).state('components', {
            url: '/components',
            templateUrl: '/home/components/components.html'
        });
});


this.commonModule = angular.module('LmApp.common', []);

this.controllersModule = angular.module('LmApp.controllers', []);

this.servicesModule = angular.module('LmApp.services', []);

this.factoriesModule = angular.module('LmApp.factories', []);

this.modelsModule = angular.module('LmApp.models', []);

this.directivesModule = angular.module('LmApp.directives', []);

this.filtersModule = angular.module('LmApp.filters', []);