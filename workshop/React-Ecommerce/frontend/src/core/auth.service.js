export class Auth{
    setStorage(name, value){
        localStorage.setItem(name,value)
    }
    setUser(user){
        this.setStorage("access_token",user.access_token);
        this.setStorage("refresh_token",user.refresh_token);
        this.setStorage("expires_in",user.expires_in)
    }
    getToken(name){
        return localStorage.getItem(name);
    }
    clearStorage(){
        localStorage.clear();
    }
}

export const AuthService = new Auth();