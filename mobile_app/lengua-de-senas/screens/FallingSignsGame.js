import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  Dimensions,
  Animated,
  Alert,
  Image
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { saveStarsToAPI, addWordToHistory, getCurrentUser } from '../services/authService';

const { width, height } = Dimensions.get('window');

/* -------------------- DATA -------------------- */

const WORDS = [
  'hola', 'adios', 'yo', 'tu', 'casa', 'mesa',
  'sol', 'luna', 'agua', 'pan', 'vida', 'amor'
];

const ALPHABET = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'
];

// Mapeo de imágenes del alfabeto
const letterImages = {
  'a': require('../assets/alfabeto/A.png'),
  'b': require('../assets/alfabeto/B.png'),
  'c': require('../assets/alfabeto/C.png'),
  'd': require('../assets/alfabeto/D.png'),
  'e': require('../assets/alfabeto/E.png'),
  'f': require('../assets/alfabeto/F.png'),
  'g': require('../assets/alfabeto/G.png'),
  'h': require('../assets/alfabeto/H.png'),
  'i': require('../assets/alfabeto/I.png'),
  'j': require('../assets/alfabeto/J.png'),
  'k': require('../assets/alfabeto/K.png'),
  'l': require('../assets/alfabeto/L.png'),
  'm': require('../assets/alfabeto/M.png'),
  'n': require('../assets/alfabeto/N.png'),
  'ñ': require('../assets/alfabeto/Ñ.png'),
  'o': require('../assets/alfabeto/O.png'),
  'p': require('../assets/alfabeto/P.png'),
  'q': require('../assets/alfabeto/Q.png'),
  'r': require('../assets/alfabeto/R.png'),
  's': require('../assets/alfabeto/S.png'),
  't': require('../assets/alfabeto/T.png'),
  'u': require('../assets/alfabeto/U.png'),
  'v': require('../assets/alfabeto/V.png'),
  'w': require('../assets/alfabeto/W.png'),
  'x': require('../assets/alfabeto/X.png'),
  'y': require('../assets/alfabeto/Y.png'),
  'z': require('../assets/alfabeto/Z.png'),
};

const WORDS_REQUIRED = 3;

/* -------------------- COMPONENT -------------------- */

export default function FallingSignsGame({ route, navigation }) {
  const { onComplete } = route.params || {};

  const [targetWord, setTargetWord] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [fallingLetters, setFallingLetters] = useState([]);
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [level, setLevel] = useState(1);
  const [fallSpeed, setFallSpeed] = useState(3200);
  const [gameOver, setGameOver] = useState(false);
  const [completedWords, setCompletedWords] = useState(0);
  const [totalStarsEarned, setTotalStarsEarned] = useState(0);

  const lettersRef = useRef([]);
  const intervalRef = useRef(null);
  const hintIntervalRef = useRef(null);
  const idRef = useRef(0);

  /* -------------------- BACKEND FUNCTIONS -------------------- */

  const saveStarsProgressToBackend = async (stars, wordsCompleted) => {
    try {
      const user = await getCurrentUser();
      if (user && user.id) {
        console.log(`💾 Guardando progreso: ${stars} estrellas, ${wordsCompleted} palabras`);
        const result = await saveStarsToAPI(user.id, stars, wordsCompleted);
        if (result.success) {
          console.log('✅ Progreso guardado en BD:', result.data);
        } else {
          console.log('⚠️ No se pudo guardar progreso:', result.mensaje);
        }
      }
    } catch (error) {
      console.error('❌ Error guardando progreso:', error);
    }
  };

  const saveWordProgressToBackend = async (word, completed, mistakes) => {
    try {
      const user = await getCurrentUser();
      if (user && user.id) {
        console.log(`📝 Guardando palabra: ${word}, completada: ${completed}`);
        const result = await addWordToHistory(user.id, word, completed, mistakes);
        if (result.success) {
          console.log('✅ Palabra guardada en historial');
        }
      }
    } catch (error) {
      console.error('❌ Error guardando palabra:', error);
    }
  };

  /* -------------------- SYNC -------------------- */

  useEffect(() => {
    lettersRef.current = fallingLetters;
  }, [fallingLetters]);

  /* -------------------- INIT -------------------- */

  useEffect(() => {
    pickNewWord();
    return () => {
      stopInterval();
      stopHintInterval();
    };
  }, []);

  useEffect(() => {
    if (targetWord && !gameOver) {
      startInterval();
    }
  }, [targetWord, gameOver, fallSpeed]);

  /* 🔑 CLAVE: reiniciar pista cuando cambia la letra */
  useEffect(() => {
    if (!gameOver && targetWord) {
      startHintInterval();
    }
  }, [currentIndex, targetWord, gameOver]);

  /* -------------------- GAME FLOW -------------------- */

  const pickNewWord = () => {
    const word = WORDS[Math.floor(Math.random() * WORDS.length)];
    setTargetWord(word);
    setCurrentIndex(0);
    clearLetters();
  };

  const startInterval = () => {
    stopInterval();
    intervalRef.current = setInterval(() => {
      if (lettersRef.current.length < 3) {
        spawnLetter(false);
      }
    }, fallSpeed / 2);
  };

  const stopInterval = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
  };

  const startHintInterval = () => {
    stopHintInterval();
    hintIntervalRef.current = setInterval(() => {
      spawnLetter(true);
    }, 15000);
  };

  const stopHintInterval = () => {
    if (hintIntervalRef.current) {
      clearInterval(hintIntervalRef.current);
      hintIntervalRef.current = null;
    }
  };

  const clearLetters = () => {
    lettersRef.current = [];
    setFallingLetters([]);
  };

  /* -------------------- SPAWN LETTER -------------------- */

  const spawnLetter = (forceCorrect = false) => {
    const expected = targetWord[currentIndex];
    if (!expected) return;

    const correctExists = lettersRef.current.some(l => l.letter === expected);
    let letter;

    if ((forceCorrect || Math.random() < 0.6) && !correctExists) {
      letter = expected;
    } else {
      const wrong = ALPHABET.filter(l => l !== expected);
      letter = wrong[Math.floor(Math.random() * wrong.length)];
    }

    const id = idRef.current++;
    const y = new Animated.Value(0);

    const item = {
      id,
      letter,
      y,
      x: Math.random() * (width - 90)
    };

    lettersRef.current.push(item);
    setFallingLetters([...lettersRef.current]);

    Animated.timing(y, {
      toValue: height,
      duration: 5000,
      useNativeDriver: false
    }).start(() => {
      lettersRef.current = lettersRef.current.filter(l => l.id !== id);
      setFallingLetters([...lettersRef.current]);
    });
  };

  /* -------------------- PRESS LETTER -------------------- */

  const handlePress = (item) => {
    if (gameOver) return;

    const expected = targetWord[currentIndex];

    if (item.letter === expected) {
      clearLetters();
      setScore(p => p + 50);

      if (currentIndex + 1 === targetWord.length) {
        // Palabra completada - otorgar 50 estrellas
        const starsForWord = 50;
        
        setCompletedWords(w => {
          const total = w + 1;
          
          // Acumular estrellas ganadas
          setTotalStarsEarned(prev => {
            const newTotal = prev + starsForWord;
            
            // Guardar palabra completada en historial
            saveWordProgressToBackend(targetWord, true, 0);
            
            if (total >= WORDS_REQUIRED) {
              stopInterval();
              stopHintInterval();
              
              // Guardar estrellas al backend
              saveStarsProgressToBackend(newTotal, total);
              
              // Llamar a onComplete con el total de estrellas ganadas
              if (onComplete) {
                onComplete(newTotal);
              }

              Alert.alert(
                '🎉 ¡Experiencia completada!',
                `Has completado ${total} palabras\n⭐ +${newTotal} estrellas ganadas en total`,
                [{ text: 'Continuar', onPress: () => navigation.goBack() }]
              );
            } else {
              Alert.alert(
                '✅ Palabra completada',
                `"${targetWord.toUpperCase()}" (${total}/${WORDS_REQUIRED})\n⭐ +${starsForWord} estrellas`,
                [{ text: 'Continuar', onPress: pickNewWord }]
              );
            }
            
            return newTotal;
          });

          return total;
        });

        setLevel(p => p + 1);
        if ((level + 1) % 3 === 0) {
          setFallSpeed(p => Math.max(1500, p - 300));
        }
      } else {
        setCurrentIndex(i => i + 1);
      }
    } else {
      setLives(p => {
        const newLives = p - 1;
        if (newLives <= 0) {
          stopInterval();
          stopHintInterval();
          setGameOver(true);

          Alert.alert(
            '💔 Game Over',
            `Palabra: ${targetWord.toUpperCase()}\nPuntos: ${score}`,
            [
              { text: 'Reintentar', onPress: restartGame },
              { text: 'Salir', onPress: () => navigation.goBack() }
            ]
          );
        }
        return newLives;
      });
    }
  };

  const restartGame = () => {
    setScore(0);
    setLives(3);
    setLevel(1);
    setFallSpeed(3200);
    setCompletedWords(0);
    setTotalStarsEarned(0);
    setGameOver(false);
    pickNewWord();
  };

  /* -------------------- RENDER -------------------- */

  return (
    <LinearGradient
      colors={['#04309e', '#0056b3', '#34a3fd', '#77c1fd', '#cfe8fa', '#ffffff']}
      style={styles.container}
      start={{ x: 0.5, y: 0 }}
      end={{ x: 0.5, y: 1 }}
    ><StatusBar barStyle="light-content" backgroundColor="#04309e" translucent={true} />
              
      <SafeAreaView style={styles.safeArea}>

        <View style={styles.header}>
          <TouchableOpacity onPress={() => navigation.goBack()}>
            <Ionicons name="close" size={30} color="#fff" />
          </TouchableOpacity>
          <Text style={styles.headerText}>
            ⭐ {totalStarsEarned}   🦜 {lives}   🎯 {level}
          </Text>
        </View>

      <View style={styles.wordRow}>
        {targetWord.split('').map((l, i) => (
          <View
            key={i}
            style={[
              styles.slot,
              i < currentIndex && styles.done,
              i === currentIndex && styles.current
            ]}
          >
            <Text style={styles.slotText}>{l.toUpperCase()}</Text>
          </View>
        ))}
      </View>

      <View style={styles.game}>
        {fallingLetters.map(item => (
          <Animated.View
            key={item.id}
            style={{
              position: 'absolute',
              left: item.x,
              transform: [{ translateY: item.y }]
            }}
          >
            <TouchableOpacity
              style={styles.bubble}
              onPress={() => handlePress(item)}
              activeOpacity={0.7}
            >
              {letterImages[item.letter] && (
                <Image
                  source={letterImages[item.letter]}
                  style={styles.letterImage}
                  resizeMode="contain"
                />
              )}
            </TouchableOpacity>
          </Animated.View>
        ))}
      </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

/* -------------------- STYLES -------------------- */
/* ❗️SIN CAMBIOS */

/* -------------------- STYLES -------------------- */

const styles = StyleSheet.create({
  container: { flex: 1 },
  safeArea: { flex: 1 },

  header: {
    height: 100,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingBottom: 1,
    
  },
  headerText: { color: '#fff', fontWeight: 'bold' },

  wordRow: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 10,
    paddingVertical: 20,
    backgroundColor: 'rgba(255, 255, 255, 0)',
    marginHorizontal: 10,
    borderRadius: 15,
  },

  slot: {
    width: 48,
    height: 55,
    borderRadius: 10,
    borderWidth: 2,
    borderColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center'
  },
  done: {
    backgroundColor: '#CF142B',
    borderColor: '#000000'
  },
  current: {
    borderColor: '#000000',
    borderWidth: 4,
    transform: [{ scale: 1.1 }]
  },
  slotText: {
    color: '#fff',
    fontSize: 22,
    fontWeight: 'bold'
  },

  game: { flex: 1 },

  bubble: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: '#CF142B',
    borderWidth: 4,
    borderColor: '#000000',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000000',
    shadowOpacity: 0.6,
    shadowRadius: 10,
    elevation: 10,
  },
  letterImage: {
    width: 110,
    height: 110,
  }
});
