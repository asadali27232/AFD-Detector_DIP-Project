import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Apple Foliar Diseases Detection</Text>
      <Text style={styles.text}>Mobile App</Text>
      <Text style={styles.text}>Under Construction</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    color: '#7fff00',
    fontSize: 30,
    fontWeight: 'bold',
  },
});
