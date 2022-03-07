import 'package:cloud_chat/common/res/dimens.dart';
import 'package:cloud_chat/common/res/strings.dart';
import 'package:cloud_chat/common/routes/routes.dart';
import 'package:cloud_chat/common/utils/consts.dart';
import 'package:cloud_chat/ui/base/base_screen.dart';
import 'package:cloud_chat/ui/stores/login/login_view_model.dart';
import 'package:cloud_chat/ui/widgets/base_text_button.dart';
import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';

const _logoSize = 200.0;

class LoginScreen extends BaseScreen<LoginViewModel> {
  final _loginController = TextEditingController();
  final _passwordController = TextEditingController();

  final _loginFocus = FocusNode();
  final _passwordFocus = FocusNode();

  LoginScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        title: Text(Strings.login.title),
      ),
      body: Column(
        children: [
          Expanded(
            flex: 3,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: const [
                Padding(
                  padding: EdgeInsets.all(Dimens.padding24),
                  child: SizedBox(
                    width: _logoSize,
                    height: _logoSize,
                    child: CircleAvatar(
                      backgroundImage: AssetImage(Consts.logoImage),
                    ),
                  ),
                ),
                Text(
                  Strings.appName,
                  style: TextStyle(
                    fontSize: Dimens.extraLargeFontSize,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            flex: 2,
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
                      onChanged: (s) => viewModel.onLoginChanged(s),
                      controller: _loginController,
                      focusNode: _loginFocus,
                      decoration: InputDecoration(
                        hintText: Strings.login.loginHint,
                        errorText: viewModel.loginError,
                      ),
                      textInputAction: TextInputAction.next,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: Dimens.padding24),
                  child: Observer(
                    builder: (_) => TextField(
                      onChanged: (s) => viewModel.onPasswordChanged(s),
                      controller: _passwordController,
                      focusNode: _passwordFocus,
                      decoration: InputDecoration(
                        hintText: Strings.login.passwordHint,
                        errorText: viewModel.passwordError,
                      ),
                      textInputAction: TextInputAction.done,
                      obscureText: true,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: Dimens.padding24),
                  child: TextButton(
                    onPressed: () => Navigator.pushNamed(context, Routes.registration),
                    child: Text(Strings.login.signUpButton),
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
                  text: Strings.login.loginButton,
                  onTap: () async {
                    final resOk = await viewModel.signIn();
                    if (resOk) {
                      Navigator.pushReplacementNamed(context, Routes.home);
                    }
                  },
                )
              ],
            ),
          )
        ],
      ),
    );
  }
}
