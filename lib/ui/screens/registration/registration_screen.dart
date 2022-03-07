import 'package:cloud_chat/common/res/dimens.dart';
import 'package:cloud_chat/common/res/strings.dart';
import 'package:cloud_chat/ui/base/base_screen.dart';
import 'package:cloud_chat/ui/stores/registration/registration_view_model.dart';
import 'package:cloud_chat/ui/widgets/base_text_button.dart';
import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:fluttertoast/fluttertoast.dart';

class RegistrationScreen extends BaseScreen<RegistrationViewModel> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _passwordAgainController = TextEditingController();

  final _emailFocus = FocusNode();
  final _passwordFocus = FocusNode();
  final _passwordAgainFocus = FocusNode();

  RegistrationScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        title: Text(Strings.registration.title),
      ),
      body: Column(
        children: [
          Expanded(
            flex: 1,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Padding(
                  padding: const EdgeInsets.symmetric(
                    horizontal: Dimens.padding24,
                    vertical: Dimens.padding16,
                  ),
                  child: Observer(
                    builder: (_) => TextField(
                      onChanged: (s) => viewModel.onEmailChanged(s),
                      controller: _emailController,
                      focusNode: _emailFocus,
                      decoration: InputDecoration(
                        hintText: Strings.registration.emailHint,
                        errorText: viewModel.emailError,
                      ),
                      textInputAction: TextInputAction.next,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: Dimens.padding24, vertical: Dimens.padding8),
                  child: Observer(
                    builder: (_) => TextField(
                      onChanged: (s) => viewModel.onPasswordChanged(s),
                      controller: _passwordController,
                      focusNode: _passwordFocus,
                      decoration: InputDecoration(
                        hintText: Strings.registration.passwordHint,
                        errorText: viewModel.passwordError,
                      ),
                      textInputAction: TextInputAction.next,
                      obscureText: true,
                    ),
                  ),
                ),
                Expanded(
                  flex: 1,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Padding(
                        padding: const EdgeInsets.symmetric(
                          horizontal: Dimens.padding24,
                          vertical: Dimens.padding16,
                        ),
                        child: Observer(
                          builder: (_) => TextField(
                            onChanged: (s) => viewModel.onPasswordAgainChanged(s),
                            controller: _passwordAgainController,
                            focusNode: _passwordAgainFocus,
                            decoration: InputDecoration(
                              hintText: Strings.registration.passwordAgainHint,
                              errorText: viewModel.passwordAgainError,
                            ),
                            textInputAction: TextInputAction.next,
                            obscureText: true,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            flex: 1,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                BaseTextButton(
                  text: Strings.registration.signUpButton,
                  onTap: () async {
                    final resOk = await viewModel.signUp();
                    if (resOk) {
                      Fluttertoast.showToast(
                        msg: Strings.registration.successfulRegistrationMsg,
                        toastLength: Toast.LENGTH_LONG,
                      );
                      Navigator.pop(context);
                    }
                  },
                )
              ],
            ),
          ),
        ],
      ),
    );
  }
}
