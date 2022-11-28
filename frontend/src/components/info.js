import React from 'react'
import Traffic from './traffic'
const Info = () => {
  return (
    <div className="px-12 py-12 md:py-20 md:flex md:flex-row md:gap-8">
          <Traffic/>
          <div className="py-4"></div>
          <div className="h-60 md:basis-2/3 rounded-xl shadow-lg text-center bg-zinc-800 text-zinc-200 ">
              Chart
          </div>
      </div>
  )
}

export default Info