import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  ScrollView,
  Dimensions,
  Image,
  Modal
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';

const { width } = Dimensions.get('window');
const cardWidth = (width - 60) / 4; // 4 columnas con espaciado
const insignias = [
    { id: 1, name: 'Salto Ángel', tipo: 'salto', req: 500 },
    { id: 2, name: 'El Ávila', tipo: 'avila', req: 1000 },
    { id: 3, name: 'Los Roques', tipo: 'roques', req: 2000 },
    { id: 4, name: 'Los Médanos de Coro', tipo: 'medanos', req: 2500 },
    { id: 5, name: 'El Turpial', tipo: 'turpial', req: 3000 },
    { id: 6, name: 'Pico Bolívar', tipo: 'pico', req: 4000 },
    { id: 7, name: 'Roraima', tipo: 'roraima', req: 5000 },
    { id: 8, name: 'Relámpago del Catatumbo', tipo: 'catatumbo', req: 6000 },
  ];
// Alfabeto completo en lengua de señas
const alphabet = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
  'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
];

// Mapeo de imágenes del alfabeto
const letterImages = {
  'A': require('../assets/alfabeto/A.png'),
  'B': require('../assets/alfabeto/B.png'),
  'C': require('../assets/alfabeto/C.png'),
  'D': require('../assets/alfabeto/D.png'),
  'E': require('../assets/alfabeto/E.png'),
  'F': require('../assets/alfabeto/F.png'),
  'G': require('../assets/alfabeto/G.png'),
  'H': require('../assets/alfabeto/H.png'),
  'I': require('../assets/alfabeto/I.png'),
  'J': require('../assets/alfabeto/J.png'),
  'K': require('../assets/alfabeto/K.png'),
  'L': require('../assets/alfabeto/L.png'),
  'M': require('../assets/alfabeto/M.png'),
  'N': require('../assets/alfabeto/N.png'),
  'Ñ': require('../assets/alfabeto/Ñ.png'),
  'O': require('../assets/alfabeto/O.png'),
  'P': require('../assets/alfabeto/P.png'),
  'Q': require('../assets/alfabeto/Q.png'),
  'R': require('../assets/alfabeto/R.png'),
  'S': require('../assets/alfabeto/S.png'),
  'T': require('../assets/alfabeto/T.png'),
  'U': require('../assets/alfabeto/U.png'),
  'V': require('../assets/alfabeto/V.png'),
  'W': require('../assets/alfabeto/W.png'),
  'X': require('../assets/alfabeto/X.png'),
  'Y': require('../assets/alfabeto/Y.png'),
  'Z': require('../assets/alfabeto/Z.png'),
};

const AlphabetIntroductionScreen = ({ navigation, route }) => {
  const [selectedLetter, setSelectedLetter] = useState(null);
  const [showImage, setShowImage] = useState(false);

  const getLetterImage = (letter) => {
    return letterImages[letter] || require('../assets/images/sena-hand.png');
  };

  const handleLetterPress = (letter) => {
    setSelectedLetter(letter);
    setShowImage(true);
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
          <Text style={styles.headerTitle}>📚 Alfabeto LSV</Text>
          <Text style={styles.headerSubtitle}>Toca una letra para ver su seña</Text>
        </View>
        <View style={{ width: 28 }} />
      </LinearGradient>

      {/* Grid de letras */}
      <ScrollView 
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        <View style={styles.grid}>
          {alphabet.map((letter, index) => (
            <TouchableOpacity
              key={letter}
              style={styles.letterCard}
              onPress={() => handleLetterPress(letter)}
              activeOpacity={0.7}
            >
              <View style={styles.cardContent}>
                <Image 
                  source={getLetterImage(letter)}
                  style={styles.letterImage}
                  resizeMode="cover"
                />
                <View style={styles.letterOverlay}>
                  <Text style={styles.letterText}>{letter}</Text>
                </View>
              </View>
            </TouchableOpacity>
          ))}
        </View>

        {/* Información adicional */}
        <View style={styles.infoCard}>
          <Ionicons name="information-circle" size={24} color="#667eea" />
          <Text style={styles.infoText}>
            Toca cualquier letra para ver su representación en Lengua de Señas Venezolana
          </Text>
        </View>
      </ScrollView>

      {/* Modal de imagen ampliada */}
      <Modal
        visible={showImage}
        transparent={true}
        animationType="fade"
        onRequestClose={() => setShowImage(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Letra: {selectedLetter}</Text>
              <TouchableOpacity 
                onPress={() => setShowImage(false)}
                style={styles.closeButton}
              >
                <Ionicons name="close-circle" size={32} color="#fff" />
              </TouchableOpacity>
            </View>

            <View style={styles.imageContainer}>
              {showImage && selectedLetter && (
                <Image
                  source={getLetterImage(selectedLetter)}
                  style={styles.fullImage}
                  resizeMode="contain"
                />
              )}
            </View>
            
            <View style={styles.modalFooter}>
              <Text style={styles.footerText}>Seña de la letra {selectedLetter} en LSV</Text>
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
  letterCard: {
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
  cardContent: {
    flex: 1,
    position: 'relative',
  },
  letterImage: {
    width: '100%',
    height: '100%',
  },
  letterOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.3)',
  },
  letterText: {
    fontSize: 42,
    fontWeight: 'bold',
    color: '#fff',
    textShadowColor: 'rgba(0, 0, 0, 0.75)',
    textShadowOffset: { width: 2, height: 2 },
    textShadowRadius: 4,
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
  imageContainer: {
    flex: 1,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  fullImage: {
    width: '100%',
    height: '100%',
  },
  modalFooter: {
    padding: 20,
    backgroundColor: '#0f3460',
    alignItems: 'center',
  },
  footerText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});

export default AlphabetIntroductionScreen;
