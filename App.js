import React, { useState, useEffect } from 'react';
import { Text, View, Button, ScrollView } from 'react-native';
import jsonData from './data.json';
import running from './running.json';
import { Audio } from 'expo-av';

const App = () => {

  const [data, setData] = useState(jsonData);
  const [lyrics, setLyrics] = useState('')
  const [index, setIndex] = useState(0)

  const [sound, setSound] = React.useState();

  async function playSound() {
    console.log('Loading Sound');
    const { sound } = await Audio.Sound.createAsync( require('./new_song4.m4a')
    );
    setSound(sound);

    console.log('Playing Sound');
    await sound.playAsync();
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
      setIndex(running.index)
    }, 1000);
    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return (
    <ScrollView>
      <Text></Text>
      <Text></Text>
      <Text style={{fontSize: 25}}>{data[index].title}</Text>
      <Text></Text>
      <Button title="Play Sound" onPress={playSound} />
      <Text></Text>
      <Text style={{fontSize: 20}}>{data[index].displaying}</Text>
    </ScrollView>
  );
};

export default App;