// GENERATED CODE - DO NOT MODIFY BY HAND

// **************************************************************************
// InjectableConfigGenerator
// **************************************************************************

import 'package:firebase_auth/firebase_auth.dart' as _i3;
import 'package:flutter_secure_storage/flutter_secure_storage.dart' as _i4;
import 'package:get_it/get_it.dart' as _i1;
import 'package:injectable/injectable.dart' as _i2;

import '../../data/services/auth/firebase_auth_service.dart' as _i8;
import '../../data/services/auth_manager/secure_auth_manager.dart' as _i6;
import '../../domain/interactors/auth/auth_interactor.dart' as _i9;
import '../../domain/services/auth/auth_service.dart' as _i7;
import '../../domain/services/auth_manager/auth_manager.dart' as _i5;
import '../../ui/stores/home/home_store.dart' as _i11;
import '../../ui/stores/home/home_view_model.dart' as _i10;
import '../../ui/stores/login/login_store.dart' as _i13;
import '../../ui/stores/login/login_view_model.dart' as _i12;
import '../../ui/stores/registration/registration_store.dart' as _i15;
import '../../ui/stores/registration/registration_view_model.dart' as _i14;
import '../../ui/stores/splash/splash_store.dart' as _i17;
import '../../ui/stores/splash/splash_view_model.dart' as _i16;
import '../modules/firebase_module.dart' as _i18;
import '../modules/secure_storage_module.dart'
    as _i19; // ignore_for_file: unnecessary_lambdas

// ignore_for_file: lines_longer_than_80_chars
/// initializes the registration of provided dependencies inside of [GetIt]
_i1.GetIt $initGetIt(_i1.GetIt get,
    {String? environment, _i2.EnvironmentFilter? environmentFilter}) {
  final gh = _i2.GetItHelper(get, environment, environmentFilter);
  final firebaseModule = _$FirebaseModule();
  final secureStorageModule = _$SecureStorageModule();
  gh.factory<_i3.FirebaseAuth>(() => firebaseModule.firebaseAuth);
  gh.lazySingleton<_i4.FlutterSecureStorage>(
      () => secureStorageModule.secureStorage);
  gh.factory<_i5.AuthManager>(
      () => _i6.SecureAuthManager(get<_i4.FlutterSecureStorage>()));
  gh.factory<_i7.AuthService>(
      () => _i8.FirebaseAuthService(get<_i3.FirebaseAuth>()));
  gh.lazySingleton<_i9.AuthInteractor>(
      () => _i9.AuthInteractor(get<_i7.AuthService>(), get<_i5.AuthManager>()));
  gh.factory<_i10.HomeViewModel>(
      () => _i11.HomeStore(get<_i9.AuthInteractor>()));
  gh.factory<_i12.LoginViewModel>(
      () => _i13.LoginStore(get<_i9.AuthInteractor>()));
  gh.factory<_i14.RegistrationViewModel>(
      () => _i15.RegistrationStore(get<_i9.AuthInteractor>()));
  gh.factory<_i16.SplashViewModel>(
      () => _i17.SplashStore(get<_i9.AuthInteractor>()));
  return get;
}

class _$FirebaseModule extends _i18.FirebaseModule {}

class _$SecureStorageModule extends _i19.SecureStorageModule {}
