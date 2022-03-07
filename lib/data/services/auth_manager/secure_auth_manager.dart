import 'package:cloud_chat/domain/services/auth_manager/auth_manager.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:injectable/injectable.dart';

const _uidKey = 'UID_KEY';

@Injectable(as: AuthManager)
class SecureAuthManager implements AuthManager {
  final FlutterSecureStorage _secureStorage;

  SecureAuthManager(this._secureStorage);

  @override
  Future<String> getToken() async => await _secureStorage.read(key: _uidKey) ?? '';

  @override
  Future saveToken(String uid) => _secureStorage.write(key: _uidKey, value: uid);

  @override
  Future<bool> authorized() async => (await getToken()).isNotEmpty;

  @override
  Future deleteToken() async {
    _secureStorage.delete(key: _uidKey);
  }
}