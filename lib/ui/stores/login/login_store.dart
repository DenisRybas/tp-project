import 'package:cloud_chat/common/res/strings.dart';
import 'package:cloud_chat/domain/interactors/auth/auth_interactor.dart';
import 'package:cloud_chat/ui/stores/login/login_view_model.dart';
import 'package:injectable/injectable.dart';
import 'package:mobx/mobx.dart';

part 'login_store.g.dart';

@Injectable(as: LoginViewModel)
class LoginStore = _LoginStore with _$LoginStore;

abstract class _LoginStore with Store implements LoginViewModel {
  @observable
  @override
  String? loginError;
  @observable
  @override
  String? passwordError;

  String _currentLogin = '';
  String _currentPassword = '';
  final AuthInteractor _interactor;

  _LoginStore(this._interactor);

  @action
  @override
  void onLoginChanged(String newValue) {
    _currentLogin = newValue;
    _clearAllErrors();
  }

  @action
  @override
  void onPasswordChanged(String newValue) {
    _currentPassword = newValue;
    _clearAllErrors();
  }

  @action
  @override
  Future<bool> signIn() async {
    if (!_validCredentials()) {
      return false;
    }
    final result = await _interactor.signIn(_currentLogin, _currentPassword);
    switch(result) {
      case AuthResult.success:
        return true;
      case AuthResult.unknownUser:
        loginError = Strings.login.unknownUser;
        break;
      case AuthResult.invalidPassword:
        passwordError = Strings.login.invalidPassword;
        break;
      case AuthResult.unverifiedEmail:
        loginError = Strings.login.unverifiedEmail;
        break;
      case AuthResult.unknownError:
        break;
    }
    return false;
  }

  void _clearAllErrors() {
    loginError = null;
    passwordError = null;
  }

  bool _validCredentials() {
    if (_currentLogin.isEmpty) {
      loginError = Strings.commonErrors.emptyField;
      return false;
    }
    if (_currentPassword.isEmpty) {
      passwordError = Strings.commonErrors.emptyField;
      return false;
    }
    return true;
  }
}
