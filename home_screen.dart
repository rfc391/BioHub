
import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _isOfflineMode = false;
  final _localStore = LocalStore();
  
  @override
  void initState() {
    super.initState();
    _initializeOfflineData();
  }
  
  Future<void> _initializeOfflineData() async {
    await _localStore.init();
    if (_isOfflineMode) {
      final cachedData = await _localStore.getCachedData();
      setState(() {
        sensorData = cachedData;
      });
    }
  }
  
  Future<void> _toggleOfflineMode(bool value) async {
    setState(() => _isOfflineMode = value);
    if (value) {
      await _localStore.cacheCurrentData(sensorData);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('FES Mobile'),
        actions: [
          Switch(
            value: _isOfflineMode,
            onChanged: (value) => setState(() => _isOfflineMode = value),
          )
        ],
      ),
      body: Column(
        children: [
          StreamBuilder(
            stream: sensorDataStream,
            builder: (context, snapshot) {
              if (!snapshot.hasData) return CircularProgressIndicator();
              return Container(
                height: 200,
                child: charts.TimeSeriesChart(snapshot.data),
              );
            },
          ),
          ElevatedButton(
            onPressed: () => _authenticateWithBiometrics(),
            child: Text('Authenticate'),
          )
        ],
      ),
    );
  }
}
