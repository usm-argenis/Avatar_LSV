import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  ScrollView,
  Dimensions,
  Modal,
  Alert
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WebView } from 'react-native-webview';
import AsyncStorage from '@react-native-async-storage/async-storage';

const { width } = Dimensions.get('window');
const cardWidth = (width - 60) / 5; // 5 columnas para números

// Números del 0 al 100
const numbers = [
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
  '20', '30', '40', '50', '60', '70', '80', '90', '100'
];

const NumbersIntroductionScreen = ({ navigation, route }) => {
  const [avatarSeleccionado, setAvatarSeleccionado] = useState('luis');

  useEffect(() => {
    loadSelectedAvatar();
  }, []);

  const loadSelectedAvatar = async () => {
    try {
      const avatar = await AsyncStorage.getItem('selectedAvatar');
      if (avatar) {
        setAvatarSeleccionado(avatar.toLowerCase());
      }
    } catch (error) {
      console.error('Error cargando avatar:', error);
    }
  };

  const [selectedNumber, setSelectedNumber] = useState(null);
  const [showAnimation, setShowAnimation] = useState(false);

  const handleNumberPress = (number) => {
    setSelectedNumber(number);
    setShowAnimation(true);
  };

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#04309e" translucent={true} />

      {/* Header */}
      <LinearGradient
        colors={['#04309e', '#0056b3', '#34a3fd', '#77c1fd', '#cfe8fa', '#ffffff']}
        style={styles.header}
        start={{ x: 0.5, y: 0 }}
        end={{ x: 0.5, y: 1 }}
      >
        <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backButton}>
          <Ionicons name="arrow-back" size={28} color="#000" />
        </TouchableOpacity>
        <View style={styles.headerContent}>
          <Text style={styles.headerTitle}>🔢 Números LSV</Text>
          <Text style={styles.headerSubtitle}>Toca un número para ver su seña</Text>
        </View>
        <View style={{ width: 28 }} />
      </LinearGradient>

      {/* Grid de números */}
      <ScrollView 
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        <View style={styles.grid}>
          {numbers.map((number, index) => (
            <TouchableOpacity
              key={number}
              style={styles.numberCard}
              onPress={() => handleNumberPress(number)}
              activeOpacity={0.7}
            >
              <LinearGradient
                colors={['#00B5E2', '#0099cc']}
                style={styles.cardGradient}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 1 }}
              >
                <Text style={styles.numberText}>{number}</Text>
                <View style={styles.iconContainer}>
                  <Ionicons name="hand-left" size={20} color="rgba(255,255,255,0.7)" />
                </View>
              </LinearGradient>
            </TouchableOpacity>
          ))}
        </View>

        {/* Información adicional */}
        <View style={styles.infoCard}>
          <Ionicons name="information-circle" size={24} color="#00B5E2" />
          <Text style={styles.infoText}>
            Toca cualquier número para ver su representación en Lengua de Señas Venezolana
          </Text>
        </View>
      </ScrollView>

      {/* Modal de animación 3D */}
      <Modal
        visible={showAnimation}
        transparent={true}
        animationType="slide"
        onRequestClose={() => setShowAnimation(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Número: {selectedNumber}</Text>
              <TouchableOpacity 
                onPress={() => setShowAnimation(false)}
                style={styles.closeButton}
              >
                <Ionicons name="close-circle" size={32} color="#fff" />
              </TouchableOpacity>
            </View>

            <View style={styles.animationContainer}>
              {showAnimation && selectedNumber && (
                <WebView
                  source={{ 
                    uri: `http://192.168.10.93:8000/lesson_simple.html?letra=${encodeURIComponent(selectedNumber)}&avatar=${avatarSeleccionado || 'luis'}&autoplay=true&v=${Date.now()}`
                  }}
                  originWhitelist={['*']}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  allowsInlineMediaPlayback={true}
                  mediaPlaybackRequiresUserAction={false}
                  style={styles.webview}
                  startInLoadingState={true}
                  renderLoading={() => (
                    <View style={styles.loadingContainer}>
                      <Text style={styles.loadingText}>Cargando animación...</Text>
                    </View>
                  )}
                />
              )}
            </View>
            
            <View style={styles.modalFooter}>
              <Text style={styles.footerText}>Seña del número {selectedNumber} en LSV</Text>
            </View>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f7fa',
  },
  header: {
    height: 100,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingTop: StatusBar.currentHeight || 30,
    paddingBottom: 10,
  },
  backButton: {
    padding: 8,
  },
  headerContent: {
    flex: 1,
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000',
    marginBottom: 4,
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#000',
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: 15,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  numberCard: {
    width: cardWidth,
    height: cardWidth,
    marginBottom: 15,
    borderRadius: 16,
    overflow: 'hidden',
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  cardGradient: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 10,
  },
  numberText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  iconContainer: {
    position: 'absolute',
    bottom: 6,
    right: 6,
  },
  infoCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 20,
    borderRadius: 16,
    marginTop: 10,
    marginBottom: 20,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
  infoText: {
    flex: 1,
    marginLeft: 12,
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.85)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    width: width * 0.9,
    height: '70%',
    backgroundColor: '#1a1a2e',
    borderRadius: 20,
    overflow: 'hidden',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#0f3460',
  },
  modalTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
  },
  closeButton: {
    padding: 4,
  },
  animationContainer: {
    flex: 1,
    backgroundColor: '#000',
  },
  webview: {
    flex: 1,
    backgroundColor: 'transparent',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#1a1a2e',
  },
  loadingText: {
    color: '#fff',
    fontSize: 16,
    marginTop: 10,
  },
  modalFooter: {
    padding: 20,
    backgroundColor: '#0f3460',
    alignItems: 'center',
  },
  footerText: {
    color: '#fff',
    fontSize: 16,
  },
});

export default NumbersIntroductionScreen;
