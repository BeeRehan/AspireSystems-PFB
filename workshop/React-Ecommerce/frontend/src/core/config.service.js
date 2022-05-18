export class ConfigService{
    baseUrl = "";
    client_id = "";
    client_secret = "";

    constructor(){
        this.init();
    }
    init(){
        this.setClientInfo();
        this.setBaseUrl();
    }
    setBaseUrl(){
        this.baseUrl = process.env.REACT_APP_BASE_URL;
    }
    setClientInfo(){
        this.client_id = process.env.REACT_APP_CLIENT_ID;
        this.client_secret = process.env.REACT_APP_CLIENT_SECRET;
    }
    getBaseUrl(){
        return this.baseUrl;
    }
    getClientInfo(){
        return{
            client_id:this.client_id,
            client_secret:this.client_secret,
        }
    }
}

export const config = new ConfigService()