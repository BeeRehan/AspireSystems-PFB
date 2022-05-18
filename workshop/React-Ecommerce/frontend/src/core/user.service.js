import { config } from "./config.service"
import { UtilService } from "utils/utils"
import { toast } from 'react-toastify';
import { AuthService } from "./auth.service";
export class User{
    auth = config.getClientInfo()
    url = config.getBaseUrl()
    accessToken = AuthService.getToken("access_token")

    siginup(userData){
        const requestBody = UtilService.convertToFormData(userData);
        const requestHeaders = {
            method:"POST",
            body:requestBody
        }
        return fetch(`${this.url}/signup`,requestHeaders)
        .then(res=>{
            if(res.ok)
            {
                return res.json()
            }
            throw res
        })
        .then(res=>{
            toast.success(res)
        })
        .catch(err=>{
            err.json().then((err)=>{
                toast.error(err)
            })
        })
    }
    signin(user){
        const requestBody = UtilService.convertToFormData(
            {
                ...user,
                ...this.auth
            }
        );
        const requestHeaders = {
            method:"POST",
            body:requestBody
        }
        return fetch(`${this.url}/signin`,requestHeaders)
        .then((res)=>
        {
            if(!res.ok){
                throw res;
            }
            return res.json();
        })
        .then((res)=>{
            toast.success("Sigin Successfully");  
            return(res)
        })
        .catch((err)=>{
            err.json().then((err)=>{
                toast.error(err); 
            })
        })
    }
    listProduct(){
        return fetch(`${this.url}/products`)
        .then((res)=>{
          if(res.ok){
            return res.json()
          }
          throw res;
        })
        .then((res)=>{
            return res;
        })
        .catch((err)=>{
          console.log(err)
        })
      }
}

export const UserService = new User();