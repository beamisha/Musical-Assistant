import React, { useState, useEffect } from 'react';
import { Text, View, Button, ScrollView } from 'react-native';
import jsonData from './data.json';
import running from './running.json';
import { Audio } from 'expo-av';

const App = () => {

  const [data, setData] = useState(jsonData)
  const [lyrics, setLyrics] = useState('')
  const [index, setIndex] = useState(running.index)
  const [sound, setSound] = useState()
  const [sound2, setSound2] = useState()
  const [interval, setInt] = useState(10000000000)
  const [tempo, setTempo] = useState(data[index].tempo)
  const [totalBeats, setBeats] = useState(1)
  const [beat, setBeat] = useState(1)

  async function playSound(metronome) {
    console.log('Loading Sound');
    if (metronome)  {
      const { sound } = await Audio.Sound.createAsync(require('./audio/9_theo_5.wav'));
      console.log('metronome loaded')
      setSound(sound);
      console.log('Playing Sound');
      await sound.playAsync();
    }
    else {
      const { sound } = await Audio.Sound.createAsync(require('./new_song10.m4a'));
      setSound2(sound);
      console.log('Playing Sound');
      await sound.playAsync();
    } 
  }

  useEffect(() => {
    return sound
      ? () => {
          console.log('Unloading Sound');
          sound.unloadAsync();
        }
      : undefined;
  }, [sound]);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setData(jsonData);
    }, 1000);
    return () => {
      clearInterval(intervalId);
    };
  }, []);

  useEffect(() => {
    const intervalId = setInterval(() => {
      //playSound(true)
      setBeats(totalBeats => totalBeats + 1)
      setBeat(beat => ((beat + 1) % 4))
      console.log(interval);
    }, interval);
    return () => {
      clearInterval(intervalId);
    };
  }, [interval]);

  const play = () => {
    setInt(60000/tempo)
    playSound(false)
  }

  const pause = () => {
    setInt(1000000000)
  }

  const reset = () => {
    setBeats(0)
    setBeat(0)
  }

  return (
    <ScrollView>
      <Text></Text>
      <Text></Text>
      <Text style={{fontSize: 25}}>{data[index].title}</Text>
      <Text></Text>
      <View style={{flex: 1, flexDirection: 'row', justifyContent: 'center', alignItems: 'center'}}>
        <Text style={{fontSize: 20}}>Bar: {Math.floor(totalBeats / 4)}</Text>
        <Text>    </Text>
        <Text style={{fontSize: 20}}>Beat: {beat + 1}</Text>
        <Text>      </Text>
        <Button title="Start" onPress={play} />
        <Button title="Stop" onPress={pause} />
        <Button title="Reset" onPress={reset} />
      <Text></Text>
      </View>
      
      <Text style={{fontSize: 20}}>{data[index].displaying}</Text>
    </ScrollView>
  );
};

export default App;