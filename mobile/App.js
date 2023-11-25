import React, { useState, useEffect } from 'react';
import {
    StatusBar,
    ImageBackground,
    TouchableOpacity,
    Image,
} from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { StyleSheet, Text, View } from 'react-native';
import ImgToBase64 from 'react-native-image-base64';

export default function App() {
    const defaultImage = require('./assets/choose.jpg');
    const [selectedImage, setSelectedImage] = useState(defaultImage);

    useEffect(() => {
        (async () => {
            const { status } =
                await ImagePicker.requestMediaLibraryPermissionsAsync();
            if (status !== 'granted') {
                alert(
                    'Sorry, we need camera roll permissions to make this work!'
                );
            }
        })();
    }, []);

    const pickImage = async () => {
        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.Images,
            allowsEditing: true,
            aspect: [4, 3],
            quality: 1,
        });

        if (!result.canceled) {
            setSelectedImage(result.assets[0]);
            // Send the image to your local API
            sendImageToApi(result.assets[0]);
        }
    };

    const sendImageToApi = async (image) => {
        console.log(image.uri, 'image uri');
        try {
            // Read the image file as base64 data
            const base64 = await ImgToBase64.getBase64String(image.uri);

            // Create an object with the base64 data
            const imageData = {
                file: base64,
                name: 'image.jpg', // You can specify a different name if needed
            };

            // Send the image data as JSON
            const response = await fetch(
                'http://127.0.0.1:5000/detector/upload',
                {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(imageData),
                }
            );

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            console.log(result, 'result');
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <ImageBackground
            source={require('./assets/bg-test2.jpg')}
            style={styles.background}>
            <View style={styles.container}>
                <View style={styles.header}>
                    <Image
                        source={require('./assets/cover.png')}
                        style={styles.header_image}
                    />
                </View>
                <Text style={styles.text}>
                    AFD Detector - Get Disease Predictions
                </Text>
                <TouchableOpacity onPress={pickImage} style={styles.box}>
                    <Image source={selectedImage} style={styles.image} />
                </TouchableOpacity>
                <View style={styles.box}>
                    <ImageBackground
                        source={require('./assets/Marijuana2.jpg')}
                        style={{ width: '100%', height: '100%' }}>
                        <View style={styles.result}>
                            <Text style={styles.result_title}>Frog Eye</Text>
                            <Text style={styles.result_text}>
                                Lorem ipsum dolor, sit amet consectetur
                                adipisicing elit. Quas quia dolore facilis!
                                Earum ad quasi similique accusamus! Dignissimos,
                                autem perspiciatis! Earum ad quasi similique
                                accusamus! Dignissimos, autem perspiciatis!
                            </Text>
                        </View>
                    </ImageBackground>
                </View>

                <StatusBar style="auto" />
            </View>
        </ImageBackground>
    );
}

const styles = StyleSheet.create({
    background: {
        resizeMode: 'cover',
        width: '100%',
        height: '100%',
    },
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'start',
    },
    text: {
        marginTop: 40,
        marginBottom: 40,
        color: 'black',
        fontSize: 18,
        fontWeight: 'bold',
        color: '#6eaf4b',
        fontFamily: 'Roboto',
    },
    header: {
        flex: 0.35,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#6eaf4b',
        width: '100%',
    },
    header_image: {
        height: 40,
        resizeMode: 'contain',
    },
    box: {
        borderColor: '#7CA966',
        borderWidth: 2,
        alignItems: 'center',
        justifyContent: 'center',
        width: '80%',
        height: '35%', // Set your fixed height for both boxes here
    },
    image: {
        width: '100%',
        height: '100%',
        resizeMode: 'cover',
    },
    result: {
        width: '100%',
        height: '100%',
        alignItems: 'center',
        justifyContent: 'start',
        resizeMode: 'cover',
        color: 'white',
        padding: 20,
    },
    result_title: {
        color: 'white',
        fontSize: 26,
        fontWeight: 'bold',
        marginBottom: 20,
        fontFamily: 'Roboto',
    },
    result_text: {
        color: 'white',
        fontSize: 18,
        textAlign: 'justify',
        fontFamily: 'Roboto',
    },
});
