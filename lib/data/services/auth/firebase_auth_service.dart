import 'package:cloud_chat/domain/services/auth/auth_service.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:injectable/injectable.dart';

@Injectable(as: AuthService)
class FirebaseAuthService implements AuthService {
  final FirebaseAuth _firebaseAuth;

  FirebaseAuthService(this._firebaseAuth);

  @override
  Future<UserCredential> signIn(String email, String password) async {
    UserCredential userCredential = await _firebaseAuth.signInWithEmailAndPassword(
      email: email,
      password: password,
    );
    return userCredential;
  }

  @override
  Future logout() => _firebaseAuth.signOut();

  @override
  Future signUpWithEmail(String email, String password) =>
    _firebaseAuth.createUserWithEmailAndPassword(email: email, password: password);
}