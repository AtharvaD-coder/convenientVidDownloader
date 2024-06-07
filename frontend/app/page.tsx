
'use client'

import { useState } from 'react';
import { PlaceholdersAndVanishInput } from '../components/ui/placeholders-and-vanish-input';
// import CustomDropdown from './components/dropdown';
// import { BackgroundBeams } from '@/components/ui/background-beams';

export default function Home() {
  const [url, setUrl] = useState('');
  // const [quality, setQuality] = useState('highest');
  const [message, setMessage] = useState('');


  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
  };

  const handleSubmit = async (e:any) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/download', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // body: JSON.stringify({ url, quality }),
      body: JSON.stringify({ url }),
    });
    const data = await response.json();
    // setMessage(data.message);
    setMessage(data);
  };

  // const handleQualityChange = (value: string) => {
  //   setQuality(value);
  // };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center py-2">
      <div onSubmit={handleSubmit} className="w-full max-w-md ">
        <h1 className="text-3xl font-bold mb-5 text-center"> Video Downloader</h1>

        <PlaceholdersAndVanishInput
        placeholders={["Enter the Youtube URL..."]}
        onChange={handleInputChange}
        onSubmit={handleSubmit}
        />

        {/* <CustomDropdown
          options={[
            { label: 'Highest Quality', value: 'highest' },
            { label: '720p', value: '720p' },
            { label: '480p', value: '480p' },
          ]}
          value={quality}
          onChange={handleQualityChange}
        />  
      
        <select
          value={quality}
          onChange={(e) => setQuality(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded mb-4"
        >
          <option value="highest">Highest Quality</option>
          <option value="720p">720p</option>
          <option value="480p">480p</option>
        </select> */}
       

        {/* <input type="file"  /> */}
        {/* <button
          type="submit"
          className="w-full bg-blue-500 text-white p-2 rounded"
        >
          Download
        </button> */}
      </div>
      {message && <p className="mt-5 text-lg text-current">Downloaded Successfully!</p>}
    </div>
  );
}