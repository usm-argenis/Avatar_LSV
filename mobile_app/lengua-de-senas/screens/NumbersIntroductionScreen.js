import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  ScrollView,
  Dimensions,
  Modal,
  Image
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';

const { width } = Dimensions.get('window');
const cardWidth = (width - 60) / 5; // 5 columnas para números

// Números del 0 al 100
const numbers = Array.from({ length: 101 }, (_, i) => i.toString());

// Mapeo de imágenes de números
const numberImages = {
  '0': require('../assets/numeros/0.png'),
  '1_D': require('../assets/numeros/1_D.png'),
  '2_D': require('../assets/numeros/2_D.png'),
  '3_D': require('../assets/numeros/3_D.png'),
  '4_D': require('../assets/numeros/4_D.png'),
  '5_D': require('../assets/numeros/5_D.png'),
  '1_I': require('../assets/numeros/1_I.png'),
  '2_I': require('../assets/numeros/2_I.png'),
  '3_I': require('../assets/numeros/3_I.png'),
  '4_I': require('../assets/numeros/4_I.png'),
  '5_I': require('../assets/numeros/5_I.png'),
};

// Función para obtener las imágenes de un número según las reglas
const getNumberImages = (number) => {
  const num = parseInt(number);
  
  // 0-5: Usar imágenes _D y el 0
  if (num === 0) return [[{ image: numberImages['0'], single: true }]];
  if (num >= 1 && num <= 5) return [[{ image: numberImages[`${num}_D`], single: true }]];
  
  // 6-10: Combinaciones con 5_I (como un solo grupo)
  if (num === 6) return [[{ image: numberImages['1_D'] }, { image: numberImages['5_I'] }]];
  if (num === 7) return [[{ image: numberImages['2_D'] }, { image: numberImages['5_I'] }]];
  if (num === 8) return [[{ image: numberImages['3_D'] }, { image: numberImages['5_I'] }]];
  if (num === 9) return [[{ image: numberImages['4_D'] }, { image: numberImages['5_I'] }]];
  if (num === 10) return [[{ image: numberImages['5_D'] }, { image: numberImages['5_I'] }]];
  
  // 11-15: Grupo del 10 + grupo de la unidad
  if (num >= 11 && num <= 15) {
    const unidad = num - 10;
    return [
      [{ image: numberImages['5_D'] }, { image: numberImages['5_I'] }], // Grupo 10
      [{ image: numberImages[`${unidad}_D`] }] // Grupo unidad
    ];
  }
  if (num >= 16 && num <= 19) {
    const unidad = num - 15;
    return [
      [{ image: numberImages['5_D'] }, { image: numberImages['5_I'] }], // Grupo 10
      [{ image: numberImages['1_D'] }, { image: numberImages[`${unidad}_I`] }] // Grupo 5+unidad
    ];
  }
  
  // 20+: Separar dígitos (23 = 2_D + 3_D)
  if (num >= 20) {
    const digits = number.toString().split('');
    const groups = [];
    digits.forEach(digit => {
      const d = parseInt(digit);
      if (d === 0) {
        groups.push([{ image: numberImages['0'] }]);
      } else if (d >= 1 && d <= 5) {
        groups.push([{ image: numberImages[`${d}_D`] }]);
      } else if (d >= 6 && d <= 9) {
        // Para 6-9, agregar la combinación como un grupo
        const base = d - 5;
        groups.push([{ image: numberImages[`${base}_D`] }, { image: numberImages['5_I'] }]);
      }
    });
    return groups;
  }
  
  return [[{ image: numberImages['0'], single: true }]];
};

const NumbersIntroductionScreen = ({ navigation, route }) => {
  const [selectedNumber, setSelectedNumber] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [visibleImages, setVisibleImages] = useState([]);

  const handleNumberPress = (number) => {
    setSelectedNumber(number);
    setShowModal(true);
    setVisibleImages([]);
    
    // Mostrar imágenes con aparición secuencial por grupos
    const groups = getNumberImages(number);
    groups.forEach((group, index) => {
      setTimeout(() => {
        setVisibleImages(prev => [...prev, index]);
      }, index * 1000); // 1000ms (1 segundo) entre cada grupo
    });
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

      {/* Modal con imágenes */}
      <Modal
        visible={showModal}
        transparent={true}
        animationType="slide"
        onRequestClose={() => setShowModal(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Número: {selectedNumber}</Text>
              <TouchableOpacity 
                onPress={() => setShowModal(false)}
                style={styles.closeButton}
              >
                <Ionicons name="close-circle" size={32} color="#fff" />
              </TouchableOpacity>
            </View>

            <View style={[
              styles.imagesContainer,
              selectedNumber && getNumberImages(selectedNumber).length === 1 && getNumberImages(selectedNumber)[0].length === 1 && styles.imagesContainerSingle,
              selectedNumber && getNumberImages(selectedNumber).length === 1 && getNumberImages(selectedNumber)[0].length === 2 && styles.imagesContainerPair
            ]}>
              {selectedNumber && getNumberImages(selectedNumber).map((group, groupIdx) => (
                visibleImages.includes(groupIdx) && (
                  <View key={groupIdx} style={[
                    styles.groupRow,
                    getNumberImages(selectedNumber).length === 1 && getNumberImages(selectedNumber)[0].length === 1 && styles.groupRowSingle,
                    getNumberImages(selectedNumber).length === 1 && getNumberImages(selectedNumber)[0].length === 2 && styles.groupRowPair
                  ]}>
                    {group.map((item, imgIdx) => (
                      <View 
                        key={`${groupIdx}-${imgIdx}`}
                        style={[
                          styles.imageWrapper,
                          item.single && styles.imageWrapperSingle,
                          group.length === 2 && getNumberImages(selectedNumber).length === 1 && styles.imageWrapperPair,
                          group.length === 2 && getNumberImages(selectedNumber).length > 1 && styles.imageWrapperPairMulti
                        ]}
                      >
                        <Image
                          source={item.image}
                          style={styles.numberImage}
                          resizeMode="contain"
                        />
                      </View>
                    ))}
                  </View>
                )
              ))}
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
  imagesContainer: {
    flex: 1,
    backgroundColor: '#fff',
    justifyContent: 'flex-start',
    alignItems: 'center',
    padding: 10,
  },
  imagesContainerSingle: {
    justifyContent: 'center',
    padding: 30,
  },
  imagesContainerPair: {
    justifyContent: 'center',
    padding: 20,
  },
  groupRow: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
    maxHeight: '45%',
    marginVertical: 5,
  },
  groupRowSingle: {
    maxHeight: '80%',
    flex: 1,
  },
  groupRowPair: {
    maxHeight: '70%',
    flex: 1,
  },
  imageWrapper: {
    flex: 1,
    aspectRatio: 0.9,
    margin: 3,
    backgroundColor: '#f5f5f5',
    borderRadius: 12,
    padding: 8,
    justifyContent: 'center',
    alignItems: 'center',
    maxHeight: 200,
  },
  imageWrapperSingle: {
    width: '80%',
    flex: 0,
    maxHeight: '100%',
    height: '100%',
  },
  imageWrapperPair: {
    flex: 1,
    maxWidth: '48%',
    maxHeight: '100%',
    height: '100%',
  },
  imageWrapperPairMulti: {
    flex: 1,
    maxWidth: '48%',
  },
  numberImage: {
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
  },
});

export default NumbersIntroductionScreen;
