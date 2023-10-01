import { defineStore } from "pinia"

export const useElementStore = defineStore("ElementStore", {
  state: () => {
    return {
      symbol: "H",
    }
  },
  actions: {
    setSymbol(symbol: string) {
      this.symbol = symbol
    },
  }
})