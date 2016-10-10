** This project currently works only on Windows. **

## In a nutshell
An improvisational AI that unleashes the creative power of an entire orchestra to music producers and artists.

## How we built it

We have built an AI orchestra, capable of improvising musical pieces in real time, inspiring and adapting to the humans it is playing with, and generating completely new songs based on its experience. We organized these three capabilities under two distinct pipelines within our platform.

Ad Hoc improvisation and procedural generation is accomplished through our Neural Pipeline. The pipeline itself is driven by two different models. One consists of a character generating Recurrent Neural Network, capable of reading audio MIDI files and learning their structure. This network can then generate creative pieces on the piano, violin, cello, and trumpets. The songs we created sound both euphonic and aggressive, very different from what a normal human would compose. After seeing these results, we became very interested about what networks designed by actual music theorists can do. This caused us to also incorporate elements of Hexahedria’s Biaxial Recurrent Network within our pipeline. This model explicitly learns pieces by using music theory and multiple recurrence dimensions (temporal and note spaces) to generate beautiful music. Those results made us very excited, thinking about the different kinds of music that different AI architectures can create.

Real-time adaptive playing is accomplished through the Improvisational Pipeline. This consists of an Arduino and two microphones (one from a set of Apple ear pods) mounted to a classical violin, which pick up the notes being played on our violin. We isolate these notes by sampling based on the beat. The note itself is determined by running a Fast Fourier Transform on the signal received and then extracting the most prominent frequency (a note is essentially a particular frequency). Finally, these extracted notes are mapped to new notes based on Music Theory, using concepts such as the pentatonic scale, perfect fourths, etc.

## How we built it

This project made extensive use of the WolframAPI and Mathematica, mainly to convert signals from the violin to midi files. We also use Mathematica to output the processed notes as various instruments in our improvisational pipeline. Finally, our Neural Pipeline took advantage of the variety and abundance of built-in instruments within Mathematica to generate distinct sound profiles for our orchestral compositions with the RNN.

The Neural module was built in tensor-flow, making extensive use of the RNN modules that were available then. The char-rnn architecture used to compose some of the songs takes into input textualized MIDI files and processes them through 2 hidden layers. After the training process, the network is able to generate textualized MIDI data, which then can be converted into actual music through the Wolfram API. The biaxial RNN consisted of two vertical stacks of LSTM-RNN nodes who were interconnected, the note and time networks, each with two hidden layers. The input would consist of a vector consisting a vector’s MIDI note alongside some information on the note’s vicinity and the history of notes played. The input would then be passed through a vanilla recurrent time axis, in order to learn some structure. Then, the output of the time network would be passed to the note axis, who makes recurrent connections alongside other Note nodes. This ensures that the network is able to learn connections between different notes and their relationship to each other throughout multiple musical pieces

The Improvisational pipeline was powered by digital signal processing. The fundamental technique in digital signal processing is the Fast Fourier Transform, a O(n log n) algorithm that is incredibly versatile in its scope and application. In our project, it allowed us to filter different notes just through their frequencies. Since FFTs are just something that the three Computer Science majors in the group had studied in theory until that point, it was incredible to see its power when implementing it to build our application.

## Challenges we ran into

Even in our demos, lag consistently hampered our efforts to sound euphonic. The best way we found to mitigate this was timing the delay so that it is always behind by a factor of the beats per minute of the violin composition. This is a fundamental limit in all sampling based approaches and requires a more sophisticated predictive model to completely eliminate.

The neural networks also had issues. The most basic one was training time since the neural networks took 10 hours to train on all of our datasets. The most crucial challenge was out of our hands though. We had several problems in making the char-RNN learn musical structure, as it would often play awkward combination of notes, spend large amounts of time not playing anything and then compressing dozens of notes in a few seconds. More training epochs helped remediate this problem, but the architecture still needs better forms of representing musical structure in order to be more effective.


## What's next for OrchestrAI

We would love to use more advanced machine learning and deep learning techniques even in our improvisational pipeline, provided delay is not a limiting factor. We would love to integrate ensembles of neural network models and see how they would play together with each other, besides adding in better ML models to the pipeline. We also want to find more ways to connect this pipeline to the human element, by maybe providing more ways for the AI to help a human generate/create music.
