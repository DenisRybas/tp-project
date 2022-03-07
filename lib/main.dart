import 'package:cloud_chat/common/routes/routes.dart';
import 'package:cloud_chat/ui/screens/home/chat_details/chat_details_screen.dart';
import 'package:cloud_chat/ui/screens/home/home_screen.dart';
import 'package:cloud_chat/ui/screens/login/login_screen.dart';
import 'package:cloud_chat/ui/screens/registration/registration_screen.dart';
import 'package:cloud_chat/ui/screens/splash/splash_screen.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

import 'di/config/injection.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  configureDependencies();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        brightness: Brightness.dark,
      ),
      initialRoute: Routes.splash,
      routes: {
        Routes.splash: (_) => SplashScreen(),
        Routes.home: (_) => HomeScreen(),
        Routes.chatDetails: (_) => ChatDetailsScreen(),
        Routes.login: (_) => LoginScreen(),
        Routes.registration: (_) => RegistrationScreen(),
      },
    );
  }
}