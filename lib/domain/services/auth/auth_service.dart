import 'package:firebase_auth/firebase_auth.dart';

abstract class AuthService {
  Future<UserCredential> signIn(String email, String password);
  Future signUpWithEmail(String email, String password);
  Future logout();
}