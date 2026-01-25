import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  SafeAreaView,
  StatusBar,
  Dimensions
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const { width } = Dimensions.get('window');

const LearningScreen = ({ navigation }) => {
  console.log('🚀 LearningScreen CARGADO - Versión con AlphabetModeSelector');
  
  const [stars, setStars] = useState(0); // Estrellas (XP) - 2000 para desbloquear nivel
  const [currentLevel, setCurrentLevel] = useState(1);

  // Módulos de aprendizaje
  const modules = [
    {
      id: 1,
      title: 'Alfabeto LSV',
      description: 'Aprende las letras A-Z',
      icon: '🔤',
      color: '#FF6B6B',
      completed: 0,
      total: 27,
      unlocked: true,
      category: 'alfabeto',
      cost: 0, // Gratis
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 2,
      title: 'Números',
      description: 'Números del 1 al 10',
      icon: '🔢',
      color: '#4ECDC4',
      completed: 0,
      total: 10,
      unlocked: stars >= 100, // Requiere 100 estrellas
      category: 'numeros',
      cost: 100,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 3,
      title: 'Saludos',
      description: 'Hola, adiós, buenos días',
      icon: '👋',
      color: '#FFE66D',
      completed: 0,
      total: 8,
      unlocked: stars >= 200,
      category: 'saludos',
      cost: 200,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 4,
      title: 'Pronombres',
      description: 'Yo, tú, él, ella, nosotros',
      icon: '👤',
      color: '#A8E6CF',
      completed: 0,
      total: 8,
      unlocked: stars >= 400,
      category: 'pronombres',
      cost: 400,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 5,
      title: 'Días de la Semana',
      description: 'Lunes a domingo',
      icon: '📅',
      color: '#FFB6C1',
      completed: 0,
      total: 7,
      unlocked: stars >= 700,
      category: 'dias_semana',
      cost: 700,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 6,
      title: 'Tiempo',
      description: 'Hoy, ayer, mañana',
      icon: '⏰',
      color: '#DDA0DD',
      completed: 0,
      total: 8,
      unlocked: stars >= 1000,
      category: 'tiempo',
      cost: 1000,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 7,
      title: 'Cortesía',
      description: 'Gracias, por favor, permiso',
      icon: '🙏',
      color: '#87CEEB',
      completed: 0,
      total: 6,
      unlocked: stars >= 1400,
      category: 'cortesia',
      cost: 1400,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    },
    {
      id: 8,
      title: 'Preguntas',
      description: '¿Cómo?, ¿Qué?, ¿Cuál?',
      icon: '❓',
      color: '#FFA07A',
      completed: 0,
      total: 5,
      unlocked: stars >= 1800,
      category: 'preguntas',
      cost: 1800,
      rewardClassic: 100,
      rewardFalling: 150,
      rewardAvatar: 150
    }
  ];

  const startLesson = (module) => {
    console.log('🎯 startLesson llamado con:', module.title, 'category:', module.category);
    
    // Si es el módulo de alfabeto, mostrar selector de modos
    if (module.category === 'alfabeto') {
      console.log('✅ Navegando a AlphabetModeSelector');
      navigation.navigate('AlphabetModeSelector', {
        moduleId: module.id,
        category: module.category,
        title: module.title
      });
    } else {
      // Para otros módulos, ir directamente a la lección
      console.log('➡️ Navegando a Lesson');
      navigation.navigate('Lesson', {
        moduleId: module.id,
        category: module.category,
        title: module.title
      });
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#667eea" />
      
      {/* Header */}
      <View style={styles.header}>
        <View style={styles.headerLeft}>
          <TouchableOpacity onPress={() => navigation.goBack()}>
            <Ionicons name="arrow-back" size={24} color="#fff" />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Aprendizaje LSV</Text>
        </View>
      </View>

      {/* Stats Bar */}
      <View style={styles.statsBar}>
        <View style={styles.statItem}>
          <Text style={styles.statIcon}>⭐</Text>
          <Text style={styles.statValue}>{stars}</Text>
          <Text style={styles.statLabel}>Estrellas</Text>
        </View>
        <View style={styles.levelProgressContainer}>
          <Text style={styles.levelText}>Nivel {currentLevel}</Text>
          <View style={styles.levelProgressBar}>
            <View 
              style={[
                styles.levelProgressFill,
                { width: `${(stars % 2000 / 2000) * 100}%` }
              ]} 
            />
          </View>
          <Text style={styles.levelProgressText}>
            {stars % 2000}/2000 para Nivel {currentLevel + 1}
          </Text>
        </View>
      </View>

      {/* BOTÓN DE TEST */}
      <TouchableOpacity 
        style={{
          backgroundColor: '#FF0000',
          padding: 20,
          margin: 15,
          borderRadius: 10,
          alignItems: 'center'
        }}
        onPress={() => {
          console.log('🔴 BOTÓN TEST PRESIONADO - Navegando a AlphabetModeSelector');
          navigation.navigate('AlphabetModeSelector', {
            moduleId: 1,
            category: 'alfabeto',
            title: 'Alfabeto LSV'
          });
        }}
      >
        <Text style={{ color: 'white', fontSize: 18, fontWeight: 'bold' }}>
          🧪 TEST - Ir a Selector de Modos
        </Text>
      </TouchableOpacity>

      {/* Modules */}
      <ScrollView 
        style={styles.scrollView}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.scrollContent}
      >
        <Text style={styles.sectionTitle}>📚 Spanish Foundations 1</Text>
        <Text style={styles.sectionSubtitle}>Aprende Lengua de Señas Venezolana</Text>

        {modules.map((module, index) => (
          <View key={module.id} style={styles.moduleContainer}>
            {/* Connector Path */}
            {index > 0 && (
              <View style={styles.connectorContainer}>
                <View style={[
                  styles.connectorPath,
                  index % 2 === 0 ? styles.connectorPathRight : styles.connectorPathLeft,
                  { borderColor: module.color }
                ]} />
              </View>
            )}

            {/* Module Card */}
            <TouchableOpacity
              style={[
                styles.moduleCard,
                { backgroundColor: module.unlocked ? module.color : '#CCCCCC' },
                !module.unlocked && styles.moduleCardLocked,
                index % 2 === 0 ? styles.moduleCardRight : styles.moduleCardLeft
              ]}
              onPress={() => module.unlocked && startLesson(module)}
              disabled={!module.unlocked}
            >
              <View style={styles.moduleIcon}>
                <Text style={styles.moduleIconText}>{module.icon}</Text>
              </View>
              
              <View style={styles.moduleInfo}>
                <Text style={styles.moduleTitle}>{module.title}</Text>
                <Text style={styles.moduleDescription}>{module.description}</Text>
                
                {/* Progress */}
                <View style={styles.progressContainer}>
                  <View style={styles.progressBar}>
                    <View 
                      style={[
                        styles.progressFill,
                        { width: `${(module.completed / module.total) * 100}%` }
                      ]} 
                    />
                  </View>
                  <Text style={styles.progressText}>
                    {module.completed}/{module.total}
                  </Text>
                </View>
              </View>

              {module.unlocked ? (
                <Ionicons name="play-circle" size={40} color="#fff" />
              ) : (
                <View style={styles.lockedContainer}>
                  <Ionicons name="lock-closed" size={30} color="#666" />
                  <View style={styles.costBadge}>
                    <Text style={styles.costIcon}>⭐</Text>
                    <Text style={styles.costText}>{module.cost}</Text>
                  </View>
                </View>
              )}
            </TouchableOpacity>

            {/* Reward Items */}
            {(index === 2 || index === 5) && (
              <View style={styles.rewardItem}>
                <Text style={styles.rewardIcon}>
                  {index === 2 ? '🏆' : '📖'}
                </Text>
              </View>
            )}
          </View>
        ))}

        {/* Bottom Spacing */}
        <View style={{ height: 100 }} />
      </ScrollView>

      {/* Bottom Navigation */}
      <View style={styles.bottomNav}>
        <TouchableOpacity style={styles.navItem} onPress={() => navigation.navigate('Home')}>
          <Ionicons name="home" size={28} color="#ccc" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="barbell" size={28} color="#ccc" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="shield" size={28} color="#667eea" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="person" size={28} color="#ccc" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="notifications" size={28} color="#ccc" />
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8F9FA',
  },
  header: {
    backgroundColor: '#667eea',
    paddingHorizontal: 20,
    paddingVertical: 15,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  headerLeft: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginLeft: 15,
  },
  statsBar: {
    flexDirection: 'row',
    backgroundColor: '#fff',
    paddingVertical: 20,
    paddingHorizontal: 20,
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
    marginBottom: 30, // Más espacio entre stats y módulos
  },
  statItem: {
    alignItems: 'center',
    marginRight: 20,
  },
  statIcon: {
    fontSize: 28,
    marginBottom: 5,
  },
  statValue: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
  },
  statLabel: {
    fontSize: 12,
    color: '#666',
    marginTop: 2,
  },
  levelProgressContainer: {
    flex: 1,
  },
  levelText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#667eea',
    marginBottom: 8,
  },
  levelProgressBar: {
    height: 12,
    backgroundColor: '#E0E0E0',
    borderRadius: 6,
    overflow: 'hidden',
  },
  levelProgressFill: {
    height: '100%',
    backgroundColor: '#FFD700',
    borderRadius: 6,
  },
  levelProgressText: {
    fontSize: 11,
    color: '#666',
    marginTop: 4,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingHorizontal: 20,
    paddingTop: 20,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  sectionSubtitle: {
    fontSize: 14,
    color: '#666',
    marginBottom: 20,
  },
  moduleContainer: {
    marginBottom: 20,
    position: 'relative',
    width: '100%',
  },
  connectorContainer: {
    height: 50,
    width: '100%',
    marginBottom: 10,
  },
  connectorPath: {
    position: 'absolute',
    top: 0,
    width: '70%',
    height: 50,
    borderWidth: 4,
    borderTopWidth: 0,
    borderBottomLeftRadius: 30,
    borderBottomRightRadius: 30,
  },
  connectorPathLeft: {
    left: '15%',
    borderRightWidth: 0,
  },
  connectorPathRight: {
    right: '15%',
    borderLeftWidth: 0,
  },
  moduleCard: {
    width: '90%',
    flexDirection: 'row',
    alignItems: 'center',
    padding: 20,
    borderRadius: 25,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.3,
    shadowRadius: 10,
    elevation: 10,
    minHeight: 120,
  },
  moduleCardLeft: {
    alignSelf: 'flex-start',
    marginLeft: '5%',
  },
  moduleCardRight: {
    alignSelf: 'flex-end',
    marginRight: '5%',
  },
  moduleCardLocked: {
    opacity: 0.7,
  },
  moduleIcon: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: 'rgba(255,255,255,0.3)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 15,
  },
  moduleIconText: {
    fontSize: 32,
  },
  moduleInfo: {
    flex: 1,
  },
  moduleTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  moduleDescription: {
  lockedContainer: {
    alignItems: 'center',
  },
  costBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFD700',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 15,
    marginTop: 5,
  },
  costIcon: {
    fontSize: 14,
    marginRight: 3,
  },
  costText: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#333',
  },
    color: '#fff',
    opacity: 0.9,
    marginBottom: 10,
  },
  progressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  progressBar: {
    flex: 1,
    height: 8,
    backgroundColor: 'rgba(255,255,255,0.3)',
    borderRadius: 4,
    marginRight: 10,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#fff',
    borderRadius: 4,
  },
  progressText: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#fff',
  },
  // ...existing code...
  rewardItem: {
    marginTop: 20,
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: '#FFD700',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  rewardIcon: {
    fontSize: 40,
  },
  bottomNav: {
    flexDirection: 'row',
    backgroundColor: '#fff',
    paddingVertical: 10,
    paddingHorizontal: 20,
    justifyContent: 'space-around',
    borderTopWidth: 1,
    borderTopColor: '#f0f0f0',
  },
  navItem: {
    padding: 10,
  },
});

export default LearningScreen;
