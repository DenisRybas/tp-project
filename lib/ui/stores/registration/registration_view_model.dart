import 'package:cloud_chat/ui/base/base_view_model.dart';

abstract class RegistrationViewModel extends BaseViewModel {
    String? get emailError;
    String? get passwordError;
    String? get passwordAgainError;

    void onEmailChanged(String newValue);
    void onPasswordChanged(String newValue);
    void onPasswordAgainChanged(String newValue);

    Future<bool> signUp();
}