import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView, Image } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';

const avatars = [
  {
    id: 'luis',
    name: 'Luis',
    img: require('../assets/avatar/Luis.png'),
    color: '#3498DB',
    description: 'Avatar masculino - Completo'
  },
  {
    id: 'duvall',
    name: 'Duvall',
    img: require('../assets/avatar/Duvall.png'),
    color: '#E67E22',
    description: 'Avatar masculino - Completo'
  },
  {
    id: 'nancy',
    name: 'Nancy',
    img: require('../assets/avatar/Nancy.png'),
    color: '#9B59B6',
    description: 'Avatar femenino - Completo'
  },
  {
    id: 'carla',
    name: 'Carla',
    img: require('../assets/avatar/Carla.png'),  
    color: '#FF6B9D',
    description: 'Avatar femenino - Completo'
  },
  {
    id: 'argenis',
    name: 'Argenis',
    img: require('../assets/avatar/Argenis.png'),
    color: '#2ECC71',
    description: 'Avatar masculino - Completo'
  }
];

export default function AvatarSelector({ selectedAvatar, onSelectAvatar, onClose }) {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Selecciona tu Avatar</Text>
        <TouchableOpacity onPress={onClose} style={styles.closeButton}>
          <Ionicons name="close" size={28} color="#333" />
        </TouchableOpacity>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.avatarGrid}>
          {avatars.map((avatar) => (
            <TouchableOpacity
              key={avatar.id}
              style={[
                styles.avatarCard,
                selectedAvatar === avatar.id && styles.avatarCardSelected
              ]}
              onPress={() => onSelectAvatar(avatar.id)}
            >
              {/* Imagen del avatar */}
              <View style={styles.avatarImageContainer}>
                <Image 
                  source={avatar.img} 
                  style={styles.avatarImage}
                  resizeMode="cover"
                />
                {selectedAvatar === avatar.id && (
                  <View style={styles.selectedOverlay}>
                    <Ionicons name="checkmark-circle" size={40} color="#4CAF50" />
                  </View>
                )}
              </View>
              
              {/* Footer con información */}
              <LinearGradient
                colors={[avatar.color + '00', avatar.color]}
                style={styles.cardFooter}
              >
                <Text style={styles.avatarName}>{avatar.name}</Text>
                <Text style={styles.description}>{avatar.description}</Text>
              </LinearGradient>
            </TouchableOpacity>
          ))}
        </View>

        <View style={styles.infoBox}>
          <Ionicons name="information-circle" size={24} color="#4A90E2" />
          <Text style={styles.infoText}>
            Selecciona tu avatar favorito. Todos están completamente animados con señas LSV.
          </Text>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    paddingTop: 30,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
  closeButton: {
    padding: 5,
  },
  scrollContent: {
    padding: 20,
  },
  avatarGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  avatarCard: {
    width: '48%',
    marginBottom: 15,
    borderRadius: 15,
    overflow: 'hidden',
    backgroundColor: '#fff',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 6,
  },
  avatarCardSelected: {
    borderWidth: 3,
    borderColor: '#4CAF50',
    elevation: 8,
    shadowOpacity: 0.3,
  },
  avatarImageContainer: {
    width: '100%',
    height: 180,
    backgroundColor: '#f5f5f5',
    position: 'relative',
  },
  avatarImage: {
    width: '100%',
    height: '100%',
  },
  selectedOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(76, 175, 80, 0.3)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  cardFooter: {
    padding: 12,
  },
  avatarName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
    textShadowColor: 'rgba(0, 0, 0, 0.5)',
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 3,
  },
  description: {
    fontSize: 12,
    color: '#fff',
    textShadowColor: 'rgba(0, 0, 0, 0.5)',
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 3,
  },
  infoBox: {
    flexDirection: 'row',
    backgroundColor: '#E3F2FD',
    padding: 15,
    borderRadius: 10,
    marginTop: 20,
    alignItems: 'center',
  },
  infoText: {
    flex: 1,
    marginLeft: 10,
    fontSize: 14,
    color: '#1976D2',
  },
});
