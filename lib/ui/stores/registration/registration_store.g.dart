// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'registration_store.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic

mixin _$RegistrationStore on _RegistrationStore, Store {
  final _$emailErrorAtom = Atom(name: '_RegistrationStore.emailError');

  @override
  String? get emailError {
    _$emailErrorAtom.reportRead();
    return super.emailError;
  }

  @override
  set emailError(String? value) {
    _$emailErrorAtom.reportWrite(value, super.emailError, () {
      super.emailError = value;
    });
  }

  final _$passwordErrorAtom = Atom(name: '_RegistrationStore.passwordError');

  @override
  String? get passwordError {
    _$passwordErrorAtom.reportRead();
    return super.passwordError;
  }

  @override
  set passwordError(String? value) {
    _$passwordErrorAtom.reportWrite(value, super.passwordError, () {
      super.passwordError = value;
    });
  }

  final _$passwordAgainErrorAtom =
      Atom(name: '_RegistrationStore.passwordAgainError');

  @override
  String? get passwordAgainError {
    _$passwordAgainErrorAtom.reportRead();
    return super.passwordAgainError;
  }

  @override
  set passwordAgainError(String? value) {
    _$passwordAgainErrorAtom.reportWrite(value, super.passwordAgainError, () {
      super.passwordAgainError = value;
    });
  }

  final _$_RegistrationStoreActionController =
      ActionController(name: '_RegistrationStore');

  @override
  void onEmailChanged(String newValue) {
    final _$actionInfo = _$_RegistrationStoreActionController.startAction(
        name: '_RegistrationStore.onEmailChanged');
    try {
      return super.onEmailChanged(newValue);
    } finally {
      _$_RegistrationStoreActionController.endAction(_$actionInfo);
    }
  }

  @override
  void onPasswordChanged(String newValue) {
    final _$actionInfo = _$_RegistrationStoreActionController.startAction(
        name: '_RegistrationStore.onPasswordChanged');
    try {
      return super.onPasswordChanged(newValue);
    } finally {
      _$_RegistrationStoreActionController.endAction(_$actionInfo);
    }
  }

  @override
  void onPasswordAgainChanged(String newValue) {
    final _$actionInfo = _$_RegistrationStoreActionController.startAction(
        name: '_RegistrationStore.onPasswordAgainChanged');
    try {
      return super.onPasswordAgainChanged(newValue);
    } finally {
      _$_RegistrationStoreActionController.endAction(_$actionInfo);
    }
  }

  @override
  String toString() {
    return '''
emailError: ${emailError},
passwordError: ${passwordError},
passwordAgainError: ${passwordAgainError}
    ''';
  }
}
